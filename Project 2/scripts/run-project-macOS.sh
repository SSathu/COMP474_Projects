#!/bin/bash

COMPOSE_BAKE=true docker-compose up --build -d
# build the project in detach mode
wait
clear 
# clears the terminal

docker attach terminal-io
# attach the container to the terminal



# NOTES:
# go in the directory of this file
# do the command ./run-project-macOS.sh
# this is for macOS

# if you get permissino issues, run this command : chmod +x run-project-macOS.sh
