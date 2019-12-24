from rest_framework import serializers
from backend.models import Vote, Token

# class name has to match the model name Seriazliers






class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        # "model" and "fields"  variable name can't be modified because they are preset or inherited that way
        model = Vote
        # We will expect all the fields except the cart because that's a foreign key.
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        # "model" and "fields"  variable name can't be modified because they are preset or inherited that way
        model = Token
        # We will expect all the fields except the cart because that's a foreign key.
        fields = '__all__'

