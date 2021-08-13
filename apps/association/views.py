from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import pagination
from rest_framework import mixins 

from .serializers import PartnerSerializer, ExecutiveSerializer, JobOfferSerializer, MessageSerializer, PostSerializer, SocialNetworkSerializer, AssociationRequestSerializer
from .models import Partner, Executive, JobOffer, Message, Post, SocialNetwork, AssociationRequest

# Create your views here.
class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.AllowAny]

class ExecutiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class JobOfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [permissions.AllowAny]

class MessageViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class SocialNetworkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class AssociationRequestViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = AssociationRequest.objects.all()
    serializer_class = AssociationRequestSerializer
    permission_classes = [permissions.AllowAny]