import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from . import models
from django.contrib.auth.models import User

class SpecialisationNode(DjangoObjectType):
    class Meta:
        model = models.Specialisation
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'langage': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
            
        }
        interfaces = (relay.Node, )
        
class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        
class ProfileNode(DjangoObjectType):
    class Meta:
        model = models.Profile
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        
        
class QuizzNode(DjangoObjectType):
    class Meta:
        model = models.Quizz
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'niveau': ['exact'],
            'pourcentage': ['exact'],
            'duree': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        
class QuestionNode(DjangoObjectType):
    class Meta:
        model = models.Question
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'niveau': ['exact'],
            'contenu': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )

class ReponseNode(DjangoObjectType):
    class Meta:
        model = models.Reponse
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'isrtue': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
        } 
        interfaces = (relay.Node, )
        
        
class QuizzUserNode(DjangoObjectType):
    class Meta:
        model = models.QuizzUser
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'note': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        
class ReponseUserNode(DjangoObjectType):
    class Meta:
        model = models.ReponseUser
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'istrue': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, ) 


class Query(graphene.ObjectType):
    Specialisation = relay.Node.Field(SpecialisationNode)
    all_Specialisation = DjangoFilterConnectionField(SpecialisationNode)

    Profile = relay.Node.Field(ProfileNode)
    all_Profiles = DjangoFilterConnectionField(ProfileNode)

    Quizz = relay.Node.Field(QuizzNode)
    all_Quizzs = DjangoFilterConnectionField(QuizzNode)

    Question = relay.Node.Field(QuestionNode)
    all_Questions = DjangoFilterConnectionField(QuestionNode)

    Reponse = relay.Node.Field(ReponseNode)
    all_Reponses = DjangoFilterConnectionField(ReponseNode)

    QuizzUser = relay.Node.Field(QuizzUserNode)
    all_QuizzUsers = DjangoFilterConnectionField(QuizzUserNode)

    ReponseUser = relay.Node.Field(ReponseUserNode)
    all_ReponseUsers = DjangoFilterConnectionField(ReponseUserNode)
