from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = '$#FHenfge24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dbBigPro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)


from application.backend import routes