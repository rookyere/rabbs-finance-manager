#!/bin/bash

# build the flask container
docker build -t rookyere/finance_manager .

# create the network
docker network create fm-net

# start the DB container
docker run --name fm_db --network fm-net -e MYSQL_DATABASE=finance_manager_db -e MYSQL_USER=fm_user -e MYSQL_PASSWORD=fm_user_pwd -e MYSQL_ROOT_PASSWORD=rookyere -p 4488:3306 -d mysql:latest

sleep 5
# start the django app container
docker run --name fm_app --network fm-net -p 8080:8000 rookyere/finance_manager
