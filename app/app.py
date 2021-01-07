from flask import Flask, jsonify, request, Response
from db.db import initialize_db
from db.models import Event
from type_data import EventKind, EventComponentTiming , PerformanceEvent
import json

app = Flask(__name__)
app.debug = True

app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb+srv://techyield:techyield@nwboardcluster.frbft.mongodb.net/test?retryWrites=true&w=majority'
}

initialize_db(app)

@app.route('/events')
def events():
    events = Event.objects.to_json()
    return Response(events, mimetype='application/json', status=200)

@app.route('/events', methods=['POST'])
def add_event():
    body = request.get_json()
    event =  Event(**body).save()    
    return jsonify(event), 200

@app.route('/events/<id>', methods=['PUT'])
def update_event(id): 
    body = request.get_json()
    Event.objects.get(id=id).update(**body)
    return '', 200

@app.route('/events/<id>', methods=['DELETE'])
def delete_event(id): 
    Event.objects.get(id=id).delete()
    return '', 200

if __name__ == '__main__':
    app.run()
