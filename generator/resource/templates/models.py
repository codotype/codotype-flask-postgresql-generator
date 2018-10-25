from mongoengine import *

<%_ /*-----------------------------------------------*/ _%>
<%_ /* """Builds each model - iterates over each schema in blueprint""" */ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ blueprint.schemas.forEach((schema) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
class <%= schema.class_name %>Model(Document):
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ schema.attributes.forEach((attr) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ if (attr.datatype === 'TEXT') { _%>
  <%= attr.identifier %> = StringField(required=<%= attr.required ? 'True' : 'False' %>, unique=<%= attr.required ? 'True' : 'False' %>, max_length=32)
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ } else if (attr.datatype === 'NUMBER') { _%>
  <%= attr.identifier %> = FloatField(required=<%= attr.required ? 'True' : 'False' %>, unique=<%= attr.required ? 'True' : 'False' %>)
<%_ } _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ }) _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ schema.relations.forEach((rel) => { _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ if (rel.type === 'BELONGS_TO' || rel.type === 'HAS_ONE') { _%>
  <%= rel.alias.identifier %> = ReferenceField('<%= rel.schema.class_name %>Model')
<%_ } else if (rel.type === 'HAS_MANY') { _%>
  <%= rel.alias.identifier %>_ids = ListField(ReferenceField('<%= rel.schema.class_name %>'))
<%_ } _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ /*-----------------------------------------------*/ _%>
<%_ }) _%>
  meta = { 'collection': '<%= schema.identifier_plural %>' }

<%_ }) _%>