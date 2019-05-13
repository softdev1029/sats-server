import graphene

import sats_server.sats_api.schema 


class Query(sats_server.sats_api.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass

schema = graphene.Schema(query=Query)