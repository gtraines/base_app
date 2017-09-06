from flask import make_response
from flask import Blueprint

blueprint = Blueprint('app', __name__)


@blueprint.route('/')
def index():
    return make_response('<h1>Return value</h1>')
