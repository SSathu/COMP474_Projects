#!/bin/bash

COMPOSE_BAKE=true docker-compose up --build -d
# build the project in detach mode

while true; do
    # checks if the terminal container is running, which is the last container to start

    if docker ps --filter "name=terminal-io" --filter "status=running" | grep -q "terminal-io"; then
        echo "Starting Chatbot..."
        docker attach terminal-io
        break
    else
        echo "Waiting for docker to build all images and run all containers"
        sleep 10
    fi
done

clear

docker exec -it terminal-io python /terminal_io/terminal_driver.py



# go in the directory of this file
# do the command ./run-project-macOS.sh
# this is for macOS

# if you get permissino issues, run this command : chmod +x run-project-macOS.sh
