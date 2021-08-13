from rest_framework import serializers
from .models import Partner, Executive, JobOffer, Message, Post, SocialNetwork, AssociationRequest

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['first_name', 'last_name']

class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['partner'] = instance.partner.get_full_name()
        representation['position'] = instance.get_position_display()
        return representation


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username
        representation['publication_date'] = instance.publication_date.strftime("%d/%m/%Y %H:%M hs")
        return representation


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username
        representation['publication_date'] = instance.publication_date.strftime("%d/%m/%Y %H:%M hs")
        return representation

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['page'] = instance.get_page_display()
        return representation

class AssociationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociationRequest
        fields = '__all__'