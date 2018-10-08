from flask.views import MethodView
import json

# CRUD Resources
class <%- schema.class_name %>CollectionResource(MethodView):
    def get(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>' })
        return body, status

    def post(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from POST /<%- schema.identifier_plural %>' })

class <%- schema.class_name %>ModelResource(MethodView):
    def get(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>/<%- schema.identifier %>_id' })
        return body, status

    def put(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from PUT /<%- schema.identifier_plural %>/<%- schema.identifier %>_id' })
        return body, status

    def delete(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from DELETE /<%- schema.identifier_plural %>/<%- schema.identifier %>_id' })
        return body, status

<%_ schema.relations.forEach((rel) => { _%>
<% if (rel.type === 'BELONGS_TO') { -%>
class <%- schema.class_name %>Related<%- rel.schema.class_name %>Resource(MethodView):
    def get(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>/<%- schema.identifier %>_id/<%- rel.schema.identifier %>' })
        return body, status

<% } else if (rel.type === 'HAS_MANY' || rel.type === 'OWNS_MANY') { -%>
class <%- schema.class_name %>Related<%- rel.schema.class_name_plural %>Resource(MethodView):
    def get(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>/<%- schema.identifier %>_id/<%- rel.schema.identifier_plural %>' })
        return body, status

<% } -%>
<% }) -%>
