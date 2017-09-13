register_model_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "User Registration",
    "description": "Schema of post data for creating a new todo \
                    in the todo app.",
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "title": "Email",
            "pattern": "^\\S+@\\S+$",
            "description": "The unique id of the todo:",
            "maxLength": 255,
            "validationMessage": "Don't be greedy!"
        },
        "firstName": {
            "type": "string",
            "description": "The unique id of user.",
            "maxLength": 255
        },
        "lastName": {
            "type": "string",
            "description": "The unique id of user.",
            "maxLength": 255
        },
        "title": {
            "type": "string",
            "description": "The title of the todo",
            "maxLength": 255
        },
        "organizationName": {
            "type": "string",
            "description": "The title of the todo",
            "maxLength": 255
        },
        "organizationAddress": {
            "type": "string",
            "description": "The title of the todo",
            "maxLength": 255
        },
        "password": {
            "type": "string",
            "description": "The title of the todo",
            "maxLength": 255
        }
    },
    "additionalProperties": False,
    "required": ["email", "password"]
}

register_form = [
    "name",
    "email",
    "firstName",
    "lastName",
    "title",
    "organizationName",
    "organizationAddress",
    {
        "key": "password",
        "type": "password",
    },
    {
        "type": "submit",
        "style": "btn-info",
        "title": "Register"
    }
]
