from .db import db 
import datetime

class Event(db.Document):
    kind = db.StringField()
    start_time = db.DateTimeField()
    end_time = db.DateTimeField()
    timestamp = db.DateTimeField(default=datetime.datetime.now())
    
