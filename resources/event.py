from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.models import Event, User
from flask_restful import Resource


class EventsApi(Resource):
    def get(self):
        events = Event.objects.to_json()
        return Response(events, mimetype='application/json', status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        event = Event(**body, added_by=user)
        event.save()
        user.update(push__events=event)
        user.save()
        id = event.id
        return {'id': str(id)}, 200


class EventApi(Resource):

    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        event = Event.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Event.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        event = Event.objects.get(id=id, added_by=user_id)
        return '', 200

    def get(self, id):
        event = Event.objects.get(id=id).to_json()
        return Response(event, mimetype="application/json", status=200)
