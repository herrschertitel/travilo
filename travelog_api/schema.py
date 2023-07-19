import graphene
import geo.schema

class Query(geo.schema.Query, graphene.ObjectType):
    pass

class Mutation(geo.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)