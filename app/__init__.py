from flask import Blueprint

def get_blueprint():
    from . import views
    blueprint = Blueprint('app', __name__)
    return blueprint

