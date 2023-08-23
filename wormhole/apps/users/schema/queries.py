import graphene

from wormhole.apps.users.schema import types
from wormhole.utils.graphql import define_query


class Queries(object):
    @define_query(graphene.Field(types.UserProfile))
    def my_profile(self, info):
        if info.context.user.is_authenticated:
            return info.context.user
