from api.endpoints.categories import ns as blog_categories_namespace
from api.endpoints.posts import ns as blog_posts_namespace
from api.restplus import api
from flask import Blueprint


def register(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    api.add_namespace(blog_categories_namespace)
    flask_app.register_blueprint(blueprint)

