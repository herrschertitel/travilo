import graphene
from graphene_django.types import DjangoObjectType
from .models import Location

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class Query(object):
    all_locations = graphene.List(LocationType)

    def resolve_all_locations(self, info, **kwargs):
        return Location.objects.all()

class CreateLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        lat = graphene.Float()
        lon = graphene.Float()
        name = graphene.String()

    def mutate(self, info, lat, lon, name):
        loc = Location(lat=lat, lon=lon, name=name)
        loc.save()
        return CreateLocation(location=loc)

class UpdateLocation(graphene.Mutation):
    data = graphene.Field(LocationType)

    class Arguments:
        id = graphene.ID()
        lat = graphene.Float()
        lon = graphene.Float()
        name = graphene.String()

    def mutate(self, info, id, lat, lon, name):
        location_update = Location.objects.get(pk=id)
        if location_update:
            location_update.lat = lat
            location_update.lon = lon
            location_update.name = name
            location_update.save()
        return UpdateLocation(data = location_update)

class DeleteLocation(graphene.Mutation):
    location = graphene.Field(LocationType)
    class Arguments:
        id = graphene.ID()
    
    def mutate(self, info, id):
        location_delete = Location.objects.get(pk=id)
        location_delete.delete()
        return None


class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()
    update_location = UpdateLocation.Field()
    delete_location = DeleteLocation.Field()