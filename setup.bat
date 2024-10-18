set FLASK_APP=main:create_app

flask db init
flask db migrate -m"Initialzing Database"
flask db upgrade
echo Server Log Start > server.log
