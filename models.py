from app import db
import datetime
from peewee import CharField, DateTimeField, IntegerField, DecimalField


class Subscriber(db.Model):
    number = CharField()
    location = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Towns(db.Model):
    country = CharField(null=True)
    county = CharField(null=True)
    easting = IntegerField(null=True)
    grid_reference = CharField(null=True)
    latitude = DecimalField(null=True)
    longitude = DecimalField(null=True)
    northing = IntegerField(null=True)
    place_name = CharField(null=True)
    postcode_area = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'uk_towns'
