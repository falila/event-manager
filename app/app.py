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
def test():
    return jsonify(events)

@app.route('/events', methods=['POST'])
def add_metric():
    metric = request.get_json()
    events.append(metric)
    return {'id':len(events)}, 200

@app.route('/events/<int:index>', methods=['PUT'])
def update_metric(index): 
    metric = request.get_json()
    events[index] = metric
    return jsonify(events[index]), 200

@app.route('/events/<int:index>', methods=['DELETE'])
def delete_metric(index): 
    events.pop(index)
    return 'None', 200


app.run()
