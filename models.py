# Frask-Graphql-MongoDB/models.py
from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,IntField
)

#Document-Object Mapper for mongodb
class Ranking(Document):
    meta = {"collection": "ranking"}
    no = IntField()
    title = StringField()
    artist = StringField()
    img = StringField()