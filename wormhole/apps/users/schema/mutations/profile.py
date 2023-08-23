import graphene

from wormhole.apps.users.models import User
from wormhole.apps.users.schema.types import UserProfile
from wormhole.utils.graphql import Error, success_or_error
from wormhole.utils.graphql.validator.decorators import validated
from wormhole.utils.models import get_input_fields


class UpdateUserProfileInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()


class UpdateUserProfileSuccess(graphene.ObjectType):
    user = graphene.Field(UserProfile)


@validated
class UpdateUserProfile(graphene.Mutation):
    class Arguments:
        input = UpdateUserProfileInput()

    Output = success_or_error(UpdateUserProfileSuccess)

    def mutate(self, info, input):
        user = info.context.user

        try:
            fields = get_input_fields(User, input)
            fields["username"] = fields["email"].strip().lower()
            User.objects.filter(id=user.id).update(**fields)

            user.refresh_from_db()

            return UpdateUserProfileSuccess(user=user)

        except Exception as e:
            return Error(message=e)
