# server.py

import falcon
import json
<%_ for (let schema of appSchema.schemas) { _%>
from resources.<%= schema.identifier_plural %> import *
<%_ } _%>

# # # # #

# TODOs
# - Add model definition w/ ORM (Mongo, Postgres)
# - Modularize the app into individual files for each resource
# - Generate .env, integrate into server
# - Integrate basic JWT authentication

# # # # #

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Add routes to resources
<% for (let schema of appSchema.schemas) { -%>
app.add_route('/<%- schema.identifier_plural %>', <%- schema.class_name %>CollectionResource())
<% for (let attr of schema.attributes) { -%>
<% if (attr.datatype === 'RELATION') { -%>
<% if (attr.datatypeOptions.relationType === 'BELONGS_TO') { -%>
app.add_route('/<%- schema.identifier_plural %>/{<%- schema.identifier %>_id}/<%- attr.datatypeOptions.schema_identifier %>', <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name %>Resource())
<% } else if (attr.datatypeOptions.relationType === 'OWNS_MANY' || attr.datatypeOptions.relationType === 'HAS_MANY') { -%>
app.add_route('/<%- schema.identifier_plural %>/{<%- schema.identifier %>_id}/<%- attr.datatypeOptions.schema_identifier_plural %>', <%- schema.class_name %>Related<%- attr.datatypeOptions.schema_class_name_plural %>Resource())
<% } -%>
<% } -%>
<% } -%>
<% } -%>

# # # # #

# Run this with
# $ pip install waitress
# $ waitress-serve --port=8000 things:app
