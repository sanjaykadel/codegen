import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from .MMMMMMMMMMModels import *
from .MMMMMMMMMMService import *

class MMMMMMMMMMType(DjangoObjectType):
    class Meta:
        model = MMMMMMMMMM

class MMMMMMMMMMInput(graphene.InputObjectType):
#s1s1s1s1s1
    id = graphene.ID()
    name = String()
    address = String()
    bank_id = Int()
    markedToDelete_ = Int()
#s1s1s1s1s1

class MMMMMMMMMM_SaveMutation(graphene.Mutation):
    class Arguments:
        data = MMMMMMMMMMInput()

    MMMMMMMMMM_Obj = graphene.Field(lambda: MMMMMMMMMMType)

    def mutate(self, info, data):
        dbMMMMMMMMMM = MMMMMMMMMMSaveService(data=data)
        return MMMMMMMMMM_SaveMutation(MMMMMMMMMM_Obj=dbMMMMMMMMMM)