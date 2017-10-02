from flask import Blueprint
from flask import make_response
from flask import render_template


bp_home = Blueprint('home', __name__)


@bp_home.route('/', methods=['GET'])
def index():
    return render_template('index.html')
