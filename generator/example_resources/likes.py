from flask.views import MethodView
import json


# CRUD Resources
class LikeCollectionResource(MethodView):
    def get(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /likes' })
        return body, status

    def post(self):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from POST /likes' })

class LikeModelResource(MethodView):
    def get(self, like_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /likes/%s' % like_id })
        return body, status

    def put(self, like_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from PUT /likes/%s' % like_id })
        return body, status

    def delete(self, like_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from DELETE /likes/%s' % like_id })
        return body, status

# # # # #

# MANY Like to ONE User
class LikeRelatedUserResource(MethodView):
    def get(self, like_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /likes/%s/user' % like_id })
        return body, status

# # # # #

# MANY Like to ONE Thing
class LikeRelatedThingResource(MethodView):
    def get(self, like_id):
        status = 200
        body = json.dumps({ 'message': 'Hi, this is from GET /likes/%s/thing' % like_id })
        return body, status
