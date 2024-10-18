Run The Setup Depending on your OS

setup.bat,
setup.bash,
or

Set the Flask Enviroment Variables

on Linux
export FLASK_APP=main:create_app

on Windows
set FLASK_APP=main:create_app

set up the Database

flask db init
flask db migrate -m "Optional Message" //The "-m" flag is optional
flask db upgrade
