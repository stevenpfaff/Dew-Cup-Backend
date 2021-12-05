from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Game
from .serializers import GameSerialzer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_games(request):
    games = Game.objects.all()
    serializer = GameSerialzer(games, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def single_game(request, game):
    if request.method == 'POST':
        serializer = GameSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        games = Game.objects.filter(game=game)
        serializer = GameSerialzer(games, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_game(request):
    if request.method == 'POST':
        serializer = GameSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)