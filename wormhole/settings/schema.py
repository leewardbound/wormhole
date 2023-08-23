import graphene

import wormhole.apps.indexer.schema
import wormhole.apps.users.schema


class Query(
    wormhole.apps.users.schema.Queries,
    wormhole.apps.indexer.schema.Queries,
    graphene.ObjectType,
):
    pass


class Mutation(
    wormhole.apps.users.schema.Mutations,
    graphene.ObjectType,
):
    pass


application_schema = graphene.Schema(query=Query, mutation=Mutation)
