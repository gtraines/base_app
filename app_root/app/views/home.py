from flask import make_response
from flask import Blueprint
from flask import render_template


bp_home = Blueprint('home', __name__)


@bp_home.route('/')
def index():
    return render_template('bootstrap_base.html')
