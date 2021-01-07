from .db import db 
import datetime

class Event(db.Document):
    kind = db.StringField()
    start_time = db.StringField()
    end_time = db.StringField()
    timestamp = db.DateTimeField(default=datetime.datetime.now())
    
