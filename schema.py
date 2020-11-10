# Frask-Graphql-MongoDB/schema.py
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Ranking as RankingModel

#Create graphQL schema
class Ranking(MongoengineObjectType):

    class Meta:
        description = "100-Rankings"
        model = RankingModel
        interfaces = (Node,)


#Define root type of 
class Query(graphene.ObjectType):
    node = Node.Field()
    all_rankings = MongoengineConnectionField(Ranking)

schema = graphene.Schema(query=Query, types=[Ranking])
