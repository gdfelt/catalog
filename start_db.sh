#!/usr/bin/env bash

# Check if docker is running
if [ "$(systemctl is-active docker)" = "active" ]; then
    echo 'Docker is running'
else
    echo 'Docker not running'
    exit 1
fi

DB_CONTAINER_NAME="catalog-db"

# Check if db is running, if not start
RUNNING=$(docker inspect --format="{{.State.Running}}" $DB_CONTAINER_NAME 2> /dev/null)
if [ $? -eq 1 ]; then
    echo "DB does not exist, running..." 
    docker run -d --name $DB_CONTAINER_NAME -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:latest
elif [ "$RUNNING" == "false" ]; then
    echo "DB is stopped, starting..."
    docker start $DB_CONTAINER_NAME
else
    echo "DB is running, doing nothing..."
fi

    
