from os import error
from flask import Flask, session, g
from flask_migrate import Migrate

import config
from extensions import db, mail
from models.UserModel import UserModel
from blueprints import user_bp, question_bp, explore_bp, xen_bp, people_bp


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(question_bp)
app.register_blueprint(explore_bp)
app.register_blueprint(xen_bp)
app.register_blueprint(people_bp)

migrate = Migrate(app, db)


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            g.user = user
        except error:
            print(error)
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
