from django.db.models import DateTimeField, FloatField, Model, TextField

class Location(Model):
    created_at = DateTimeField(auto_now_add=True)
    lat = FloatField()
    lon = FloatField()
    name = TextField(blank=True)
    updated_at = DateTimeField(auto_now=True)
    model = FloatField()