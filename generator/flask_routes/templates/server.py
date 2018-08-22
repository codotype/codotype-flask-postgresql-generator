# server.py

from flask import Flask
from flask.views import MethodView
import json
<%_ for (let schema of appSchema.schemas) { _%>
from resources.<%= schema.identifier_plural %> import *
<%_ } _%>

# # # # #

# TODOs (leftover from Falcon server.py)
# - Add model definition w/ ORM (Mongo, Postgres)
# - Modularize the app into individual files for each resource
# - Generate .env, integrate into server
# - Integrate basic JWT authentication

# # # # #

# Assign the Flask instance (a WSGI application) to the app variable.
app = Flask(__name__)

# Add routes to resources
<% for (let schema of appSchema.schemas) { -%>
app.add_url_rule('/api/<%- schema.identifier_plural %>', view_func=<%- schema.class_name %>CollectionResource.as_view('<%- schema.identifier_plural %>_collection_resource'), methods=['GET', 'POST'])
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>', view_func=<%- schema.class_name %>ModelResource.as_view('<%- schema.identifier_plural %>_model_resource'), methods=['GET', 'PUT', 'DELETE'])
<% for (let attr of schema.attributes) { -%>
<% if (attr.datatype === 'RELATION') { -%>
<% if (attr.datatypeOptions.relationType === 'BELONGS_TO') { -%>
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>/<%- attr.datatypeOptions.schema_identifier %>', view_func=<%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name %>Resource.as_view('<%- schema.identifier %>_related_<%- attr.datatypeOptions.schema_identifier %>_resource'), methods=['GET'])
<% } else if (attr.datatypeOptions.relationType === 'OWNS_MANY' || attr.datatypeOptions.relationType === 'HAS_MANY') { -%>
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>/<%- attr.datatypeOptions.schema_identifier_plural %>', view_func=<%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name_plural %>Resource.as_view('<%- schema.identifier %>_related_<%- attr.datatypeOptions.schema_identifier_plural %>_resource'), methods=['GET'])
<% } -%>
<% } -%>
<% } -%>
<% } -%>

if __name__ == '__main__':
    app.run(debug=True)
