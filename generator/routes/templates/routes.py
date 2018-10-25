from app import api
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /* """IMPORTS DEPENDENCIES - Iterates over each schema in blueprint""" */ _%>
<%_ blueprint.schemas.forEach((schema) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
from resources.<%= schema.identifier %> import <%= schema.class_name %>CollectionResource
from resources.<%= schema.identifier %> import <%= schema.class_name %>ModelResource
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /* """Iterates over each schema in blueprint""" */ _%>
<%_ schema.relations.forEach((rel) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ if (rel.type === 'BELONGS_TO' || rel.type === "HAS_ONE") { _%>
from resources.<%= schema.identifier %> import <%= schema.class_name %>Related<%= rel.alias.class_name %>Resource
<%_ } else { _%>
from resources.<%= schema.identifier %> import <%= schema.class_name %>Related<%= rel.alias.class_name_plural %>Resource
<%_ } _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ }) _%>
<%_ }) _%>
<%_ /* """ADDS ROUTES FOR DEPENDENCIES - Iterates over each schema in blueprint""" */ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /* """Iterates over each schema in blueprint""" */ _%>
<%_ blueprint.schemas.forEach((schema) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>

# /api/<%= schema.identifier_plural %>
api.add_route('/api/<%= schema.identifier_plural %>', <%= schema.class_name %>CollectionResource())
api.add_route('/api/<%= schema.identifier_plural %>/{<%= schema.identifier %>_id}', <%= schema.class_name %>ModelResource())
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /* """Iterates over each relation on the schema""" */ _%>
<%_ schema.relations.forEach((rel) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
api.add_route('/api/<%= schema.identifier_plural %>/{<%= schema.identifier %>_id}/<%= rel.alias.identifier %>', <%= schema.class_name %>Related<%= rel.alias.class_name %>Resource())
<%_ } else { _%>
api.add_route('/api/<%= schema.identifier_plural %>/{<%= schema.identifier %>_id}/<%= rel.alias.identifier_plural %>', <%= schema.class_name %>Related<%= rel.alias.class_name_plural %>Resource())
<%_ } _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ }) _%>
<%_ }) _%>