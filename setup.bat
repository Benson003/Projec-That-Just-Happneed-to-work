set FLASK_APP=main:create_app

python -m flask db init
python -m flask db migrate -m"Initialzing Database"
python -m flask db upgrade
echo Server Log Start > server.log
