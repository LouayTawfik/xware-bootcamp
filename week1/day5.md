## Exercise 1: Week1

## Install Postgresql.

## run the below command to update the package list on your Ubuntu server.
* >>>  sudo apt update

## Install the PostgreSQL packages by executing the below command. This command will also install the postgresql-contrib 
* >>> sudo apt install -y postgresql postgresql-contrib

## After the installation, verify the Postgres installation status by running the below command.
* >>> sudo dpkg --status postgresql

## Run the following command to create a file named /etc/apt/sources.list.d/pgdg.list. This file contains PostgreSQL’s official repository’s address specific to your Ubuntu server version.
* >>> sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

## Once the installation completes, run the below systemctl command to start the PostgreSQL service.
* >>> sudo systemctl start postgresql.service

## Finally, verify the PostgreSQL status by running the below command.
* >>> sudo systemctl status postgresql.service

## Log in to the PostgreSQL shell (psql) by running the below command.
* >>> sudo -u postgres psql
## Run the following command at the prompt to initiate a password change. Provide a strong password of your choice and press Enter.
* >>> \password

## to exit
* >>> \q or exit

## Restart the PostgreSQL server for the changes to take effect.
* >>> sudo systemctl restart postgresql

## Reconnect to the PostgreSQL server as the postgres user.
* >>> sudo -u postgres psql


================================================================================================================================================================


## Connect to pgAdmin.

## run the below command to update the package list on your Ubuntu server.
* >>> $ sudo apt-get update

## Use the next command given to add pgAdmin repository in your Ubuntu system:
* >>> $ sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

## Finally, update the package lists.
* >>> $ sudo apt update

## To install pgAdmin4 packages on Ubuntu, run this command, providing correct version number:
* >>> $ sudo apt install pgadmin4


=================================================================================================================================================================


## Clone Your Repo 'xware-bootcamp'
* >>> git clone https://github.com/LouayTawfik/xware-bootcamp.git

## Create Folder `Week1` if Not Exists.
* >>> mkdir Week1

## Create File `Day5.md` Inside `Week1` Folder.
* >>> touch Day5.md









