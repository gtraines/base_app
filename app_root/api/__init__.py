from .endpoints.categories import ns as blog_categories_namespace
from .endpoints.posts import ns as blog_posts_namespace
from .restplus import api
from app_root.core import error_handlers
from flask import Blueprint
from flask_jsonschema import ValidationError


def get_blueprint():
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    api.add_namespace(blog_categories_namespace)
    blueprint.register_error_handler(ValidationError, error_handlers.on_validation_error)

    return blueprint
