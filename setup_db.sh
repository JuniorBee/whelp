#!/usr/bin/env bash

. ./docker_setup/vars.env

# First, create a database for your project:
psql postgresql://doadmin:axfbkve48m3k2g8p@mallexpress-demo-db-do-user-6548569-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require << EOF
    CREATE DATABASE ${DB_NAME};
    CREATE USER ${DB_USER_NAME} WITH PASSWORD '${DB_PASSWORD}';
    ALTER ROLE ${DB_USER_NAME} SET client_encoding TO 'utf8';
    ALTER ROLE ${DB_USER_NAME} SET default_transaction_isolation TO 'read committed';
    ALTER ROLE ${DB_USER_NAME} SET timezone TO 'UTC+4';
    GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER_NAME};
EOF