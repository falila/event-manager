from flask import Flask, jsonify, request
from type_data import EventKind, EventComponentTiming , PerformanceEvent

app = Flask(__name__)
app.debug = True

events = [
    {"tag": "ams_sold",
    "type":" event type 1",
    "env": "dev",
    "data": ["timestamp", "created"],
    "timestamp":"time",
    },
    {"tag": "vehicle_info_updated",
    "type":" event type 2",
    "env": "test",
    "data": ["timestamp", "created"],
    "timestamp":"time",
    },
]

@app.route('/events')
def events():
    return jsonify(events)

@app.route('/events', methods=['POST'])
def add_event():
    event = request.get_json()
    events.append(event)
    return {'id':len(events)}, 200

@app.route('/events/<int:index>', methods=['PUT'])
def update_event(index): 
    event = request.get_json()
    events[index] = event
    return jsonify(events[index]), 200

@app.route('/events/<int:index>', methods=['DELETE'])
def delete_event(index): 
    events.pop(index)
    return 'None', 200


app.run()
