from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime


class Event(db.Document):
    kind = db.StringField()
    start_time = db.StringField()
    end_time = db.StringField()
    timestamp = db.DateTimeField(default=datetime.datetime.now())
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True, max_length=254)
    password = db.StringField(required=True, min_length=6)
    events = db.ListField(db.ReferenceField(
        'Event', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Event, 'added_by', db.CASCADE)
