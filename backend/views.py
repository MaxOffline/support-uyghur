from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from backend.serializers import VoteSerializer, TokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers as sers
from backend import serializers
from backend.models import Vote as v, Token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response



# Create your views here.
class index(View):

    def get(self, request):
                return render(request, "frontend/static/index.html", {})


class Vote(APIView):

    serializer_class = serializers.VoteSerializer
    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
                agree = serializer.validated_data.get('agree')
                disagree = serializer.validated_data.get('disagree')
                votes = v.objects.get(id = 1)
                votes.agree += agree
                votes.disagree += disagree
                votes.save()
                return Response("allow", status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenView(APIView):
    serializer_class = serializers.TokenSerializer

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
                tok = serializer.validated_data.get('token')
                try:
                    found = Token.objects.get(token = tok)
                    return Response("allow", status = status.HTTP_200_OK)
                except:
                    new_token = Token.objects.create(token = tok )
                    new_token.save()
                    return Response("allow", status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckIfTokenExists(APIView):
    serializer_class = serializers.TokenSerializer

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
                tok = serializer.validated_data.get('token')
                try:
                    found_token = Token.objects.get(token = tok)
                    return Response("allow", status = status.HTTP_200_OK)
                except:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetTotalVotes(APIView):

    serializer_class = serializers.VoteSerializer
    def get(self, request):
        serializer = VoteSerializer(data=request.data)
        try:
            votes = v.objects.all()
            votes = sers.serialize("json", votes)
            return Response(votes, status = status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


