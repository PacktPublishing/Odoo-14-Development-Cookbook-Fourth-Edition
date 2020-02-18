# Setting up Odoo as a system service 

### As root, create a file called `/lib/systemd/system/odoo.service` with the following contents:
```bash
[Unit]
Description=Odoo 132.0
After=postgresql.service
[Service]
Type=simple
User=odoo
Group=odoo
WorkingDirectory=/home/odoo/odoo-prod/project
ExecStart=/home/odoo/odoo-prod/project/bin/start-odoo
[Install]
WantedBy=multi-user.target
```

### As root, register the service: 

```bash
systemctl enable odoo.service
```

After that you can start and stop odoo with given commands

```bash
service odoo start
```

```bash
service odoo stop
```
