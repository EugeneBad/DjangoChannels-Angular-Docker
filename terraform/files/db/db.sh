#!/bin/bash -e
# This script automates the installation of postgresql on an Ubuntu-xenial linux machine.

install_pg(){
sudo apt-get update; sudo apt-get -y install postgresql postgresql-client postgresql-contrib
}

create_user(){
sudo -u postgres psql postgres -c "CREATE DATABASE djchannels"
sudo -u postgres psql postgres -c "CREATE USER djchannels WITH PASSWORD 'djchannels'"
sudo -u postgres psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE djchannels to djchannels"
}

install_adminpack(){
sudo -u postgres psql postgres -c "CREATE EXTENSION adminpack"
}

config_pg(){
echo "host    all             all             0.0.0.0/0            md5" | sudo tee -a /etc/postgresql/9.5/main/pg_hba.conf
echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/9.5/main/postgresql.conf

}

start_pg_on_boot(){
sudo systemctl enable postgresql
}

main(){
  install_pg
  create_user
  install_adminpack
  config_pg
  start_pg_on_boot
}
main