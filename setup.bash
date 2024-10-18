#!/bin/bash

export FLASK_APP=main:create_app

flask db init
flask db migrate -m"Initialized Database"
flask db upgrade

echo Server Log Start > server.log
