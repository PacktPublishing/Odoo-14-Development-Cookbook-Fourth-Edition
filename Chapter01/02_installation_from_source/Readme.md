# Execute given commands one by one to install Odoo

### Fetch the updates:
`sudo apt-get update`

### Run the following commands to install the main dependencies:
`sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools`

### Download and install wkhtmltopdf:
`wget  -O https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb`

`sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb `

If you find errors in previous command, force install the dependencies with given command.

`sudo apt-get install -f`

### Now, install and configure PostgreSQL database:
`sudo apt install postgresql`

`sudo -u postgres createuser --superuser $(whoami)`

### Configure git:

`git config --global user.name "Your Name"`

`git config --global user.email youremail@example.com`

### Clone the Odoo code base:

`mkdir ~/odoo-dev`

`cd ~/odoo-dev`

`git clone -b 13.0 --single-branch --depth 1 https://github.com/odoo/odoo.git `

### Create an venv-oodoo-13.0 virtual environment and activate it:
`python3 -m venv ~/venv-odoo-13.0`

`source ~/venv-odoo-13.0/bin/activate`

### Install the Python dependencies of Odoo in venv:

`cd ~/odoo-dev/odoo/`

`pip3 install wheel`

`pip3 install -r requirements.txt`

### Create and start your first Odoo instances:

`createdb odoo-test`

`python3 odoo-bin -d odoo-test –i base --addons-path=addons --db-filter=odoo-test$`
