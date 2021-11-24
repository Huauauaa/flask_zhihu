from flask import Blueprint, render_template

bp = Blueprint('explore', __name__, url_prefix='/explore')


@bp.route('/')
def index():
    return 'todo'
