from flask import Blueprint, g
from decorators import login_required
from models.UserModel import UserModel

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route('/<string:username>')
@login_required
def profile(username):
    user = UserModel.query.filter_by(username=username).first_or_404()
    return str(user.id)
