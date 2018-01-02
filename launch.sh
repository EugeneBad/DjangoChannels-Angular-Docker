#!/bin/bash
# Install angular dependencies
cd angular
npm install

#Build the javascript artifacts
ng build --prod

# Build and run docker containers
cd ..
docker-compose up -d
echo "App Launched Successfully!"
