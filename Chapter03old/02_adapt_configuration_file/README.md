# Adapting the configuration file for production

### Create a new configuration file for production based on the development file:

```bash
cd ~/odoo-prod/project

cp development.conf production.conf
```

### Update the `addons_path` in configuration file
List all the add-ons directory that you want to load in production instance. Example for,
```bash
addons_path = /home/odoo/odoo-prod/project/src/odoo/addons,
/home/odoo/odoo-prod/project/src/odoo/odoo/addons,
/home/odoo/odoo-prod/project/src/partner-contact
```

### Change the data directory:
This directory will used as filestore for your Odoo instance. This will store all attachments and assets files.

### Change the server log path:
This file path will be used to store server access logs.
```bash
logfile = /home/odoo/odoo-prod/project/logs/odoo.log
```

You can use given parameter to filter logs
```bash
log_level = warn
log_handler = :WARNING,werkzeug:CRITICAL,odoo.service.server:INFO
```

### Update database parameter
If you are hosting your database on different server then update given configuration based on that.
```bash
db_host = False
db_maxconn = 64
db_name = odoo-project
db_password = False
db_port = False
db_template = template1
db_user = False
```

### Configure the database filter and disable the database listing:
```
dbfilter = my-odoo-dbodoo-project$
list_db = False
```

### Change DB master password

``` bash
admin_password = use a random password
```

### Configure workers for performance
Number of workers are based on number of CPU core on server.
>Rule `No. of workers = CPU core * 2 +1`
```bash
workers = 4
# limit_memory_hard: 4GB
limit_memory_hard = 4294967296
# limit_memory_soft: 640MB
limit_memory_soft = 671088640
limit_request = 8192
limit_time_cpu = 120
```
