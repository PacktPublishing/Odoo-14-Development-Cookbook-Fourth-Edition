# Configuring a reverse proxy and SSL

### As root, install the Let's Encrypt client, certbot:

```bash
apt-get update
apt-get install software-properties-common
add-apt-repository universe
add-apt-repository ppa:certbot/certbot
apt-get update
apt-get install certbot python-certbot-nginx
```

### As root, request a certificate from Let's Encrypt (don't forget to change the email and the address of the server):

```bash
certbot certonly --standalone -n --agree-tos -m youremail@example.com -d odoo.example.com
```

### Create a nginx configuration file in /etc/nginx/sites-available/odoo-ssl:
```bash
upstream odoo {
    server 127.0.0.1:8069;
}
upstream odoochat {
    server 127.0.0.1:8072;
}

server {
    listen 80;
    server_name yourdomain.com;
    rewrite 301 ^(.*) https://$host$1 permanent;
}

server {

    listen 443;
    server_name odoo.example.comyourdomain.com;

    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;

    # SSL Configuration ssl on;
    ssl_certificate /etc/letsencrypt/live/odoo.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/odoo.example.com/privkey.pem;
    ssl_session_timeout 30m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    # Add log files
    access_log /var/log/nginx/odoo.access.log;][]
    error_log /var/log/nginx/odoo.error.log;

    # enable gzip
    gzip on;
    gzip_types text/css text/plain text/xml application/xml application/json application/javascript application/x-font-ttf image/svg+xml;

    # Add Headers for odoo proxy mode
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP $remote_addr;

    # Manage longpolling on 8072 port
    location /longpolling {
        proxy_pass http://odoochat;
    }

    location / {
        proxy_redirect off;
        proxy_pass http://odoo;
    }

    # Enable static cache
    location ~* /web/static/ {
        proxy_cache_valid 200 60m;
        proxy_buffering on; expires 864000;
        proxy_pass http://odoo;
    }
}
```

### create symbolic link of configuration and restart the nginx:

```bash
ln -s /etc/nginx/sites-available/odoo-ssl\ /etc/nginx/sites-enabled/odoo-ssl
```

```bash
service nginx restart
```
