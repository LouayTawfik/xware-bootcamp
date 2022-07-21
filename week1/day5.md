# Day 5.
# Install Postgresql.

* >>>  sudo apt update
* >>> sudo apt install -y postgresql postgresql-contrib
* >>> sudo dpkg --status postgresql
* >>> sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
* >>> sudo systemctl start postgresql.service
* >>> sudo systemctl status postgresql.service
* >>> sudo -u postgres psql
* >>> sudo systemctl restart postgresql
* >>> sudo -u postgres psql


# Install pgAdmin.
* >>> $ sudo apt-get update
* >>> $ sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
* >>> $ sudo apt install pgadmin4
