from flask import make_response
from flask import Blueprint

bp_home = Blueprint('home', __name__)


@bp_home.route('/')
def index():
    return make_response('<h1>Return value</h1>')
