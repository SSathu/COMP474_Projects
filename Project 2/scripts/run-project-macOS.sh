#!/bin/bash

COMPOSE_BAKE=true docker-compose up --build -d
# build the project in detach mode

clear 
# clears the terminal

docker start -a terminal-io
# runs the terminak container in attach mode



# NOTES:
# go in the directory of this file
# do the command ./run-project-macOS.sh
# this is for macOS

# if you get permissino issues, run this command : chmod +x run-project-macOS.sh
