from flask import Blueprint
from decorators import login_required

bp = Blueprint('xen', __name__, url_prefix='/xen')


@bp.route('/vip-web')
@login_required
def vip_web():
    return 'todo'
