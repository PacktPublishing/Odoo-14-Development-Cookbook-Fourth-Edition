# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.http_routing.models.ir_http import slug


class Main(http.Controller):
    @http.route('/books', type='http', auth="public", website=True)
    def library_books(self):
        country_id = False
        country_code = request.session.geoip and request.session.geoip.get('country_code') or False
        if country_code:
            country_ids = request.env['res.country'].sudo().search([('code', '=', country_code)])
            if country_ids:
                country_id = country_ids[0].id
        domain = ['|', ('restrict_country_ids', '=', False), ('restrict_country_ids', 'not in', [country_id])]
        return request.render(
            'my_library.books', {
                'books': request.env['library.book'].search([]),
            })

    def sitemap_books(env, rule, qs):
        Books = env['library.book']
        dom = sitemap_qs2dom(qs, '/books', Books._rec_name)
        for f in Books.search(dom):
            loc = '/books/%s' % slug(f)
            if not qs or qs.lower() in loc:
                yield {'loc': loc}

    @http.route('/books/<model("library.book"):book>', type='http', auth="public", website=True, sitemap=sitemap_books)
    def library_book_detail(self, book):
        return request.render(
            'my_library.book_detail', {
                'book': book,
                'main_object': book
            })

    @http.route('/books/submit_issues', type='http', auth="user", website=True)
    def books_issues(self, **post):
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            issue_description = post.get('issue_description')
            request.env['book.issue'].sudo().create({
                'book_id': book_id,
                'issue_description': issue_description,
                'submitted_by': request.env.user.id
            })
            return request.redirect('/books/submit_issues?submitted=1')

        return request.render('my_library.books_issue_form', {
            'books': request.env['library.book'].search([]),
            'submitted': post.get('submitted', False)
        })
