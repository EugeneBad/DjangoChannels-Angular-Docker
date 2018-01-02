# DjangoChannels-Angular-Docker
[Channels](https://channels.readthedocs.io/en/stable/) is an official Django project that future-proofs Django by making it able to handle
more than just plain HTTP requests, including WebSockets and HTTP2.
This project; which is a stripped down implementation of WhatsApp web; demonstrates this by having an [Angular 2](https://angular.io/) frontend making Websocket connections to a Django backend to support
real time bidirectional, full-duplex communication between the client and backend.

## Running the application
The recommended way to run the application is to use the launch bash script; open a terminal and run:
`. launch.sh`
This will build the angular javascript files and go on to create the docker containers and network
to serve up the application.
For this to work several requirements have to be met:
* [Python](https://www.python.org/downloads/) and [Nodejs](https://nodejs.org/en/download/package-manager/) have to be installed.
* Make sure Docker is installed and it's daemon running.

With the application running, navigate to (http://localhost) and have fun!

Alternatively, you can run the application in  a rather crude way without using docker

* Open up a terminal and after cloning the repo, create a python `virtualenv` and run  
`pip install -r ./backend/requirements.txt`

* Run `python manage.py runserver 0.0.0.0:8000` to run the Django backend.

* Open another terminal and navigate to `repo/angular` and run  
`npm install`.

* Run `ng serve` to run the frontend on `localhost:4200` which you can navigate to in your browser.

**NB:** Assuming Nodejs and Python already installed.
