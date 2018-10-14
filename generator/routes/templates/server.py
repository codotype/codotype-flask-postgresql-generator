# server.py

from flask import Flask
from flask.views import MethodView
import json
<%_ blueprint.schemas.forEach((schema) => { _%>
from resources.<%= schema.identifier_plural %> import *
<%_ }) _%>

# # # # #

# TODOs (leftover from Falcon server.py)
# - Add model definition w/ ORM (Mongo, Postgres)
# - Modularize the app into individual files for each resource
# - Generate .env, integrate into server
# - Integrate basic JWT authentication

# # # # #

# Assign the Flask instance (a WSGI application) to the app variable.
app = Flask(__name__)

<%_ blueprint.schemas.forEach((schema) => { _%>
# <%= schema.label_plural %> Routes
app.add_url_rule('/api/<%- schema.identifier_plural %>', view_func=<%- schema.class_name %>CollectionResource.as_view('<%- schema.identifier_plural %>_collection_resource'), methods=['GET', 'POST'])
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>', view_func=<%- schema.class_name %>ModelResource.as_view('<%- schema.identifier_plural %>_model_resource'), methods=['GET', 'PUT', 'DELETE'])
<%_ schema.relations.forEach((rel) => { _%>
<%_ if (rel.type === 'BELONGS_TO') { _%>
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>/<%- rel.schema.identifier %>', view_func=<%- schema.class_name %>Related<%- rel.schema.class_name %>Resource.as_view('<%- schema.identifier %>_related_<%- rel.schema.identifier %>_resource'), methods=['GET'])
<%_ } else if (rel.type === 'OWNS_MANY' || rel.type === 'HAS_MANY') { _%>
app.add_url_rule('/api/<%- schema.identifier_plural %>/<<%- schema.identifier %>_id>/<%- rel.schema.identifier_plural %>', view_func=<%- schema.class_name %>Related<%- rel.schema.class_name_plural %>Resource.as_view('<%- schema.identifier %>_related_<%- rel.schema.identifier_plural %>_resource'), methods=['GET'])
<%_ } _%>
<%_ }) _%>
<%_ }) _%>

if __name__ == '__main__':
    app.run(debug=True)
