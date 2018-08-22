import falcon
import json

# CRUD Resources
class <%- schema.class_name %>CollectionResource(object):
    """Handles GET requests"""
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({ "message": "Hi, this is from GET /item" })

    def on_post(self, req, resp):
      resp.status = falcon.HTTP_200  # This is the default status
      resp.body = json.dumps({ "message": "Hi, this is from POST /item" })

class <%- schema.class_name %>ModelResource(object):
    def on_get(self, req, resp, like_id):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({ "message": "Hi, this is from GET /items/:id" })

    def on_put(self, req, resp, like_id):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({ "message": "Hi, this is from PUT /items/:id" })

    def on_delete(self, req, resp, like_id):
      resp.status = falcon.HTTP_200  # This is the default status
      resp.body = json.dumps({ "message": "Hi, this is from DELETE /items/:id" })

<% for (let attr of schema.attributes) { -%>
<% if (attr.datatype === 'RELATION') { -%>
<% if (attr.datatypeOptions.relationType === 'BELONGS_TO') { -%>
class <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name %>Resource(object):
    def on_get(self, req, resp, like_id):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({ "message": "Hi, this is from GET /items/:id/foo" })
<% } else if (attr.datatypeOptions.relationType === 'HAS_MANY' || attr.datatypeOptions.relationType === 'OWNS_MANY') { -%>
class <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name_plural %>Resource(object):
    def on_get(self, req, resp, like_id):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({ "message": "Hi, this is from GET /items/:id/foo" })
<% } -%>
<% } -%>
<% } -%>
