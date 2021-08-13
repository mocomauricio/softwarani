from django.urls import path, include
from rest_framework import routers
from .views import PartnerViewSet, ExecutiveViewSet, JobOfferViewSet, MessageViewSet, PostViewSet, SocialNetworkViewSet, AssociationRequestViewSet
from .ajax import save_token

router = routers.DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'executives', ExecutiveViewSet)
router.register(r'joboffers', JobOfferViewSet)
router.register(r'posts', PostViewSet)
router.register(r'socialmedia', SocialNetworkViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'associationrequest', AssociationRequestViewSet)

urlpatterns =  [
	path('save-token/', save_token, name='save_token'),
	path('', include(router.urls))
]