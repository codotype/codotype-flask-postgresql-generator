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

<% for (let attr of schema.attributes) { -%>
<% if (attr.datatype === 'RELATION') { -%>
<% if (attr.datatypeOptions.relationType === 'BELONGS_TO') { -%>
class <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name %>Resource(MethodView):
    def get(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>/<%- schema.identifier %>_id/<%- attr.datatypeOptions.schema_identifier %>' })
        return body, status
        
<% } else if (attr.datatypeOptions.relationType === 'HAS_MANY' || attr.datatypeOptions.relationType === 'OWNS_MANY') { -%>
class <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name_plural %>Resource(MethodView):
    def get(self, <%- schema.identifier %>_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /<%- schema.identifier_plural %>/<%- schema.identifier %>_id/<%- attr.datatypeOptions.schema_identifier_plural %>' })
        return body, status

<% } -%>
<% } -%>
<% } -%>
