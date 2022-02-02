from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'ahmad'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ansariyan'
app.config['MYSQL_DATABASE_DB'] = 'dbSDLPi'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
