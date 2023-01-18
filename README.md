


# Odoo 14 Development Cookbook - Fourth Edition

<a href="https://www.packtpub.com/product/odoo-14-development-cookbook-fourth-edition/9781800200319?utm_source=github&utm_medium=repository&utm_campaign=9781800200319"><img src="https://static.packt-cdn.com/products/9781800200319/cover/smaller" alt="Odoo 14 Development Cookbook - Fourth Edition" height="256px" align="right"></a>

This is the code repository for [Odoo 14 Development Cookbook - Fourth Edition](https://www.packtpub.com/product/odoo-14-development-cookbook-fourth-edition/9781800200319?utm_source=github&utm_medium=repository&utm_campaign=9781800200319), published by Packt.

**Rapidly build, customize, and manage secure and efficient business apps using Odoo's latest features**

## What is this book about?
With its latest release, the powerful Odoo framework released a wide variety of features for rapid application development. This updated Odoo development cookbook will help you explore the new features in Odoo 14 and learn how to use them to develop Odoo applications from scratch. You’ll learn about the new website concepts in Odoo 14 and get a glimpse of Odoo's new web-client framework OWL (Odoo Web Library). 

This book covers the following exciting features:
* Build beautiful websites with Odoo CMS using dynamic building blocks
* Get to grips with advanced concepts such as caching, prefetching, debugging
* Modify backend JavaScript components and POS applications with the new OWL framework
* Connect and access any object in Odoo via Remote Procedure Calls (RPC)
* Manage, deploy, and test an Odoo instance with Odoo.sh
* Configure IoT Box to add and upgrade Point of Sale (POS) hardware
* Find out how to implement in-app purchase services

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800200315) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
@http.route('/my_library/books/json', type='json', auth='none')
def books_json(self):
    records = request.env['library.book'].sudo().search([])
    return records.read(['name'])
```

**Following is what you need for this book:**
This book is suitable for both newcomers and experienced Odoo developers who want to develop a highly efficient business application with the Odoo framework. Basic knowledge of Python and JavaScript is necessary to get the most out of the book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-24).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-24  | Odoo v14 | Ubuntu recommended (or any version of Linux) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800200319_ColorImages.pdf).

### Related products
* The Art of CRM [[Packt]](https://www.packtpub.com/product/the-art-of-crm/9781789538922?utm_source=github&utm_medium=repository&utm_campaign=9781789538922) [[Amazon]](https://www.amazon.com/dp/1789538920)

* Mastering Object-Oriented Python - Second Edition [[Packt]](https://www.packtpub.com/product/mastering-object-oriented-python-second-edition/9781789531367?utm_source=github&utm_medium=repository&utm_campaign=9781789531367) [[Amazon]](https://www.amazon.com/dp/1789531365)

## Get to Know the Author
**Parth Gajjar**
is an Odoo expert with a deep understanding of the Odoo framework. He started his career at Odoo and spent 7 years in the R&D department at Odoo India. During his time at Odoo, he worked on several key features, including a marketing automation app, mobile application, report engine, domain builder, and more. He also worked as a code reviewer and helped manage the code quality of the new features. Later, he started his own venture named Droggol and now provides various development services related to Odoo. He loves working on Odoo and solving real-world business problems with different technologies. He often gives technical training to Odoo developers.

**Alexandre Fayolle**
started working with Linux and free software in the mid-1990s and quickly became interested in the Python programming language. In 2012, he joined Camptocamp to share his expertise on Python, PostgreSQL, and Linux with the team implementing Odoo. He currently manages projects for Camptocamp and is strongly involved in the Odoo Community Association. In his spare time, he likes to play jazz on the vibraphone.

**Holger Brunn**
has been a fervent open source advocate since he came into contact with the open source market sometime in the nineties.
He has programmed for ERP and similar systems in different positions since 2001. For the last 10 years, he has dedicated his time to TinyERP, which became OpenERP and evolved into Odoo. Currently, he works at Therp BV in the Netherlands as a developer and is an active member of the Odoo Community Association.

**Daniel Reis**
has had a long career in the IT industry, largely as a consultant implementing business applications in a variety of sectors, and today works for Securitas, a multinational security services provider.
He has been working with Odoo (formerly OpenERP) since 2010, is an active contributor to the Odoo Community Association projects, is currently a member of the board of the Odoo Community Association, and collaborates with ThinkOpen Solutions, a leading Portuguese Odoo integrator.

## Other books by the authors
[Odoo 11 Development Cookbook - Second Edition](https://www.packtpub.com/application-development/odoo-11-development-cookbook-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788471817)

[Odoo Development Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/odoo-development-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781785883644)
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800200319">https://packt.link/free-ebook/9781800200319 </a> </p>