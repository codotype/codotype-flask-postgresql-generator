import falcon
import json
from mongoengine import *
from bson import ObjectId
from models import <%= schema.class_name %>Model

# Handles /api/<%= schema.identifier_plural %>
class <%= schema.class_name %>CollectionResource():

    # GET /api/<%= schema.identifier_plural %>
    def on_get(self, req, resp):

        collection = []

        for <%= schema.identifier %> in <%= schema.class_name %>Model.objects:
            model = {
                'id': str(<%= schema.identifier %>.id),
                <%_ schema.attributes.forEach((attr) => { _%>
                <%_  _%>
                <%_  _%>
                <%_ if (attr.datatype === 'TEXT') { _%>
                '<%= attr.identifier %>': <%= schema.identifier %>.<%= attr.identifier %>,
                <%_  _%>
                <%_  _%>
                <%_ } else if (attr.datatype === 'NUMBER') { _%>
                '<%= attr.identifier %>': <%= schema.identifier %>.<%= attr.identifier %>,
                <%_ } _%>
                <%_  _%>
                <%_  _%>
                <%_ }) _%>
                <%_  _%>
                <%_  _%>
                <%_ schema.relations.forEach((rel) => { _%>
                <%_  _%>
                <%_  _%>
                <%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
                '<%= rel.alias.identifier %>_id': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.id),
                '<%= rel.alias.identifier %>': {
                    'id': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.id),
                    '<%= rel.related_lead_attribute %>': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.<%= rel.related_lead_attribute %>)
                },
                <%_ } else if (rel.type === 'HAS_MANY') { _%>
                '<%= rel.alias.identifier %>_id': <%= schema.identifier %>.<%= rel.alias.identifier %>_id
                <%_ } _%>
                <%_  _%>
                <%_  _%>
                <%_ }) _%>
            }

            # Adds the model to the collection sent to the client
            collection.append(model)

        resp.json = collection
        resp.status = falcon.HTTP_200

    # POST /api/<%= schema.identifier_plural %>
    def on_post(self, req, resp):

        <%_ schema.attributes.forEach((attr) => { _%>
        <%_  _%>
        <%_  _%>
        <%_ if (attr.datatype === 'TEXT') { _%>
        <%= attr.identifier %> = req.get_json('<%= attr.identifier %>', dtype=str)
        <%_  _%>
        <%_  _%>
        <%_ } else if (attr.datatype === 'NUMBER') { _%>
        <%= attr.identifier %> = req.get_json('<%= attr.identifier %>', dtype=float)
        <%_ } _%>
        <%_  _%>
        <%_  _%>
        <%_ }) _%>
        <%_ schema.relations.forEach((rel) => { _%>
        <%_  _%>
        <%_  _%>
        <%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
        <%= rel.alias.identifier %>_id = req.get_json('<%= rel.alias.identifier %>_id', dtype=str)
        <%_ } else if (rel.type === 'HAS_MANY') { _%>
        <%= rel.alias.identifier %>_ids = req.get_json('<%= rel.alias.identifier %>_id', dtype=float)
        <%_ } _%>
        <%_  _%>
        <%_  _%>
        <%_ }) _%>

        # Creates a new <%= schema.class_name %>Model instance
        new<%= schema.class_name %> = <%= schema.class_name %>Model(
            <%_ schema.attributes.forEach((attr) => { _%>
            <%_  _%>
            <%_  _%>
            <%_ if (attr.datatype === 'TEXT') { _%>
            <%= attr.identifier %> = <%= attr.identifier %>,
            <%_  _%>
            <%_  _%>
            <%_ } else if (attr.datatype === 'NUMBER') { _%>
            <%= attr.identifier %> = <%= attr.identifier %>,
            <%_ } _%>
            <%_  _%>
            <%_  _%>
            <%_ }) _%>
            <%_ schema.relations.forEach((rel) => { _%>
            <%_  _%>
            <%_  _%>
            <%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
            <%= rel.alias.identifier %> = ObjectId(<%= rel.alias.identifier %>_id),
            <%_ } else if (rel.type === 'HAS_MANY') { _%>
            <%= rel.alias.identifier %>_ids = <%= rel.alias.identifier %>_ids
            <%_ } _%>
            <%_  _%>
            <%_  _%>
            <%_ }) _%>
        )

        # Saves the new <%= schema.class_name %>Model
        new<%= schema.class_name %>.save()

        # Sends response to client
        resp.json = {
            'id': str(new<%= schema.class_name %>.id),
            <%_ schema.relations.forEach((rel) => { _%>
            <%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
            '<%= rel.alias.identifier %>_id': <%= rel.alias.identifier %>_id,
            <%_ } else if (rel.type === 'HAS_MANY') { _%>
            '<%= rel.alias.identifier %>_ids': <%= rel.alias.identifier %>_ids,
            <%_ } _%>
            <%_ }) _%>
        }
        resp.status = falcon.HTTP_201

# Handles /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id
class <%= schema.class_name %>ModelResource():

    # GET /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id
    def on_get(self, req, resp, <%= schema.identifier %>_id):
        <%= schema.identifier %> = <%= schema.class_name %>Model.objects.get(id=<%= schema.identifier %>_id)
        model = {
            'id': str(<%= schema.identifier %>.id),
            <%_ schema.attributes.forEach((attr) => { _%>
            <%_  _%>
            <%_  _%>
            <%_ if (attr.datatype === 'TEXT') { _%>
            '<%= attr.identifier %>': <%= schema.identifier %>.<%= attr.identifier %>,
            <%_  _%>
            <%_  _%>
            <%_ } else if (attr.datatype === 'NUMBER') { _%>
            '<%= attr.identifier %>': <%= schema.identifier %>.<%= attr.identifier %>,
            <%_ } _%>
            <%_  _%>
            <%_  _%>
            <%_ }) _%>
            <%_  _%>
            <%_  _%>
            <%_ schema.relations.forEach((rel) => { _%>
            <%_  _%>
            <%_  _%>
            <%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
            '<%= rel.alias.identifier %>_id': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.id),
            '<%= rel.alias.identifier %>': {
                'id': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.id),
                '<%= rel.related_lead_attribute %>': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.<%= rel.related_lead_attribute %>)
            },
            <%_ } else if (rel.type === 'HAS_MANY') { _%>
            '<%= rel.alias.identifier %>_id': <%= schema.identifier %>.<%= rel.alias.identifier %>_id
            <%_ } _%>
            <%_  _%>
            <%_  _%>
            <%_ }) _%>
        }

        resp.json = model
        resp.status = falcon.HTTP_200

    # PUT /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id
    def on_put(self, req, resp, <%= schema.identifier %>_id):
        resp.json = { 'message': 'Hi, this is from PUT /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id' }
        resp.status = falcon.HTTP_200

    # DELETE /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id
    def on_delete(self, req, resp, <%= schema.identifier %>_id):
        resp.json = { 'message': 'Hi, this is from DELETE /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id' }
        resp.status = falcon.HTTP_200

<%_ schema.relations.forEach((rel) => { _%>
<%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>


# GET /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id/<%= rel.alias.identifier %>
class <%= schema.class_name %>Related<%= rel.alias.class_name %>Resource():
    def on_get(self, req, resp, <%= schema.identifier %>_id):

        <%_ let relatedSchema = blueprint.schemas.find(s => s._id === rel.related_schema_id) _%>
        <%= schema.identifier %> =  <%= schema.class_name %>Model.objects.get(id=<%= schema.identifier %>_id)
        <%= rel.alias.identifier %> = {
            'id': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.id),
            <%_ relatedSchema.attributes.forEach((attr) => { _%>
            <%_ if (attr.datatype === "TEXT") { _%>
            '<%= attr.identifier %>': str(<%= schema.identifier %>.<%= rel.alias.identifier %>.<%= attr.identifier %>),
            <%_ } _%>
            <%_ }) _%>
        }

        resp.json = <%= rel.alias.identifier %>
        resp.status = falcon.HTTP_200

<%_ } else { _%>
# GET /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id/<%= rel.schema.identifier_plural %>
class <%= schema.class_name %>Related<%= rel.alias.class_name_plural %>Resource():
    def on_get(self, req, resp, <%= schema.identifier %>_id):
        resp.json = { 'message': 'Hi, this is from GET /api/<%= schema.identifier_plural %>/<%= schema.identifier %>_id/<%= rel.schema.identifier_plural %>' }
        resp.status = falcon.HTTP_200

<%_ } _%>
<%_ }) _%>
