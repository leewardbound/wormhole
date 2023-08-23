from graphene_django import DjangoObjectType

from wormhole.apps.users import models


class UserProfile(DjangoObjectType):
    class Meta:
        model = models.User
        fields = [
            "id",
            "is_staff",
            "email",
            "username",
            "first_name",
            "last_name",
        ]
