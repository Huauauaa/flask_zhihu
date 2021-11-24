# Flask

## Init

- `mkdir <projectName> && cd $_`

### create and activate virtual env

- `python3 -m venv venv`

- `. venv/bin/activate`

### install [Flask](https://flask.palletsprojects.com/en/2.0.x/)

`pip install Flask`

### create `.flaskenv`

```text
FLASK_APP=app
FLASK_ENV=delelopment
FLASK_DEBUG=1
```

### create `.env`

```text
DB_USERNAME=
DB_PASSWORD=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_DEFAULT_SENDER=
```

### enable dotenv

`pip install python-dotenv`

### Run

`flask run`

## Database

### mysql

```sql
create database zhihu;
```

### config.py

```python
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhihu'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI

- [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

```

### install dependency

`pip install flask-sqlalchemy flask-migrate pymysql`

### init db

`flask db init`

### migrate when update model

`flask db migrate`

### create/update table in database

`flask db upgrade`

## email

### install [Flask-Mail](https://pythonhosted.org/Flask-Mail/)

`pip install Flask-Mail`

```python
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

from flask_mail import Mail
mail = Mail()

mail.init_app(app)
```

## install [wtforms](https://wtforms.readthedocs.io/en/3.0.x/)

`pip install WTForms`

### example

```python
from extensions import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
```

### CRUD

> refer to code

## how to use

- `pip install -r requirements.txt`
- `flask db init`
- `flask db migrate`
- `flask db upgrade`
- create `.env` and complete it
- `flask run`
