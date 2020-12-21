# Standardizing your instance directory layout

### Create one directory per instance:

```bash
mkdir ~/odoo-dev/projectname
cd ~/odoo-dev/projectname
```

### Create a Python virtual environment in a subdirectory called `env/`:
```bash
 python3 -m venv env
```

### Create some subdirectories, as follows:

```bash
$ mkdir src local bin filestore logs
```

### Clone Odoo and install the requirements:
```bash
git clone -b 13.0 --single-branch --depth 1 https://github.com/odoo/odoo.git src/odoo
```

```bash
env/bin/pip3 install -r src/odoo/requirements.txt
```

### Save the following shell script as bin/odoo:
```bash
#!/bin/sh ROOT=$(dirname $0)/..
PYTHON=$ROOT/env/bin/python3 ODOO=$ROOT/src/odoo/odoo-bin
$PYTHON $ODOO -c $ROOT/projectname.cfg "$@" exit $? \
```

### Make the script executable:
```bash
$ chmod +x bin/odoo
```

### Create an empty dummy local module:
```bash
mkdir -p local/dummy
touch local/dummy/__init__.py
echo '{"name": "dummy", "installable": False}' >\ local/dummy/  __manifest__.py
```

### Generate a configuration file for your instance:
```bash
$ bin/odoo --stop-after-init --save --addons-path src/odoo/odoo/addons,src/odoo/addons,local --data-dir filestore
```

### Add a `.gitignore` file with given content:
```bash
# dotfiles, with exceptions:
.*
!.gitignore
# python compiled files
*.py[co]
# emacs backup files
*~
# not tracked subdirectories
/env/
/src/
/filestore/
/logs/
```

### Create a Git repository for this instance:
 ```bash
git init
git add .
git commit -m "initial version of projectname"
```