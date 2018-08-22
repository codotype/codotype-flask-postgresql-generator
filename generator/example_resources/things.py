from flask.views import MethodView
import json


# CRUD Resources
class ThingCollectionResource(MethodView):
    def get(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /things' })
        return body, status
        
    def post(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from POST /things' })
        return body, status

class ThingModelResource(MethodView):
    def get(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /things/%s' % thing_id })
        return body, status
    
    def put(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from PUT /things/%s' % thing_id })
        return body, status
        
    def delete(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from DELETE /things/%s' % thing_id })
        return body, status
        

# # # # #

# MANY Thing to ONE User
    
class ThingRelatedUserResource(MethodView):
    def get(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /things/%s/user' % thing_id })
        return body, status

# # # # #

# ONE Thing to ONE PhysicalThing
class ThingRelatedPhysicalThingResource(MethodView):
    def get(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /things/%s/physical' % thing_id })
        return body, status

# # # # #

# ONE Thing to MANY Likes
class ThingRelatedLikesResource(MethodView):
    def get(self, thing_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /things/%s/likes' % thing_id })
        return body, status
