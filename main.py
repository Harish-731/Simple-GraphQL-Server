import json
import graphene
from flask import Flask, request
from graphene import ObjectType

app = Flask(__name__)

class Query(ObjectType):
    hello = graphene.String(first_name=graphene.Argument(graphene.String,default_value="stranger"))
    def resolve_hello(self, context, args, info):
        return 'Hello {}!'. format(args['first_name'])

schema = graphene.Schema(query=Query)

app.route("/graphql", methods=['POST'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)

