from app import db
import datetime
from peewee import CharField, DateTimeField, IntegerField, DecimalField,\
                 TextField
from playhouse.signals import Model as SignalledModel
from playhouse.signals import post_save
from stathat import StatHat

stats = StatHat('bwghughes@gmail.com')


class Caller(db.Model, SignalledModel):
    number = CharField()
    called_at = DateTimeField(default=datetime.datetime.now)


class Subscriber(db.Model, SignalledModel):
    number = CharField()
    location = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)


class Town(db.Model):
    country = CharField(null=True)
    county = CharField(null=True)
    easting = CharField(null=True)
    grid_reference = CharField(null=True)
    latitude = CharField(null=True)
    longitude = CharField(null=True)
    northing = CharField(null=True)
    place_name = CharField(null=True)
    postcode_area = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'uk_towns'


class Alert(db.Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    expires_at = DateTimeField()
    location = CharField()
    drug = CharField()
    message = TextField()


# Signals
@post_save(sender=Subscriber)
def on_subscriber_save_handler(sender, instance, created):
    subscriber_count = Subscriber.select().count() + 1
    print subscriber_count
    stats.count('badbatch/subscriber_count', subscriber_count)

@post_save(sender=Caller)
def on_caller_save_handler(sender, instance, created):
    caller_count = Caller.select().count() + 1
    print caller_count
    stats.count('badbatch/caller_count', caller_count)