from .endpoints.posts import ns as blog_posts_namespace
from .restplus import api
from flask import Blueprint

from .endpoints.categories import ns as blog_categories_namespace


def get_blueprint():
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    api.add_namespace(blog_categories_namespace)

    return blueprint
