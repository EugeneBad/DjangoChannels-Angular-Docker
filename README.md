# DjangoChannels-Angular-Docker
[Channels](https://channels.readthedocs.io/en/stable/) is an official Django project that future-proofs Django by making it able to handle
more than just plain HTTP requests, including WebSockets and HTTP2.
This project; which is a stripped down implementation of WhatsApp web; demonstrates this by having an [Angular 2](https://angular.io/) frontend making Websocket connections to a Django backend to support
real time bidirectional, full-duplex communication between the client and backend.

## Running in development
For now the project is not dockerised yet and an automation script is on it's way, 
but that does not mean it can't be run (crudely though):

* Open up a terminal and after cloning the repo, create a python `virtualenv` and run  
`pip install -r ./backend/requirements.txt`

* Run `python manage.py runserver` to run the Django backend.

* Open another terminal and navigate to `repo/angular` and run  
`npm install`.

* Run `ng serve` to run the frontend on `localhost:4200` which you can navigate to in your browser.

