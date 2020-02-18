# Execute given commands one by one to install Odoo for production servers
Note that, this is just a example installation. Actual production server configuration can be different based on your requirement.

> Execute commands as a root user or use sudo.

### Fetch the updates:
```bash
apt-get update
```

### Run the following commands to install the main dependencies:
```bash
apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools
```

### Download and install wkhtmltopdf:

```bash
wget  -O https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
```

```bash
dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
```

If you find errors in previous command, force install the dependencies with given command.

```bash
apt-get install -f
```

### Create new user
As root, create a user called odoo.

```bash
adduser odoo
```
### Now, install and configure PostgreSQL database:
```bash
apt install postgresql -y
```

```bash
sudo -u postgres createdb -O odoo odoo_project
```

### As user `odoo` clone the project repository

```bash
su odoo

mkdir ~/odoo-prod

cd ~/odoo-prod

git clone https://github.com/yourlogin/project.git project

mkdir -p project/src
```

### As the odoo user, clone the Odoo source code:

```bash
cd project/src

git clone -b 13.0 --single-branch https://github.com/odoo/odoo.git odoo
```

### Create an venv-odoo-13.0 virtual environment and activate it:

```bash
python3 -m venv ~/venv-odoo-13.0

source ~/venv-odoo-13.0/bin/activate
```

### Install the Python dependencies of Odoo in venv:

```bash
cd ~/odoo-dev/odoo/

pip3 install wheel

pip3 install -r requirements.txt
```

### Clone third-party add-on repositories in the project/src subdirectory (if any):

```bash
git clone -b 132.0 https://github.com/OCA/partner-contact.git
```

### Create the `~/odoo-prod/project/bin` directory:

```bash
$ mkdir ~/odoo-prod/project/bin
```

### Create a script to easily start Odoo in the production environment in ~/odoo-prod/project/bin/start-odoo:

``` bash
#!/bin/sh

PYTHON=~venv-odoo-132.0/bin/python3

ODOO=~odoo/odoo-prod/project/src/odoo/odoo-bin CONF=~odoo/odoo-prod/project/production.conf

${PYTHON} ${ODOO} -c ${CONF} "$@"
```

### Make the script executable:

```
$ chmod +x ~/odoo-prod/project/bin/start-odoo
```