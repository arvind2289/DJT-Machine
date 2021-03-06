import graphene
import graphql_jwt
import items.schema
import users.schema


# Query for getting the data from the server.
class Query(users.schema.Query, items.schema.Query, graphene.ObjectType):
    pass

# Mutation for sending the data to the server.
class Mutation(users.schema.Mutation, items.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)