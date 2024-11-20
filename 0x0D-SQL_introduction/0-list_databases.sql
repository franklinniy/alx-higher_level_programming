#!/bin/bash

# MySQL username and password
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

# MySQL command to list databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"

