# Setting up log rotation

### Create/Open the log rotate configuration file with the given command:

```bash
nano /etc/logrotate.d/odoo
```

### Add given content in `odoo` file:

```bash
/home/odoo/odoo-prod/project/logs/odoo.log {
    rotate 10
    daily
    notifempty
    missingok
    compress
    delaycompress
}
```

That’s it. Now server log generated from Odoo will generate one log file daily.