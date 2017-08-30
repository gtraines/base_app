import logging

from core.data_model.models import Category
from flask import request
from flask_restplus import Resource

from api.restplus import api
from api.serializers import category, category_with_posts
from core.business import create_category, delete_category, update_category

log = logging.getLogger(__name__)

ns = api.namespace('categories', description='Operations related to core categories')


@ns.route('/')
class CategoryCollection(Resource):

    @api.marshal_list_with(category)
    def get(self):
        """
        Returns list of core categories.
        """
        categories = Category.query.all()
        return categories

    @api.response(201, 'Category successfully created.')
    @api.expect(category)
    def post(self):
        """
        Creates a new core category.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        return Category.query.filter(Category.id == id).one()

    @api.expect(category)
    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates a core category.

        Use this method to change the name of a core category.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Category Name"
        }
        ```

        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_category(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes core category.
        """
        delete_category(id)
        return None, 204
