from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Player
from .serializers import PlayerSerialzer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_players(request):
    players = Player.objects.all()
    serializer = PlayerSerialzer(players, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_player(request, name):
    if request.method == 'POST':
        serializer = PlayerSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        players = Player.objects.filter(name=name)
        serializer = PlayerSerialzer(players, many=True)
        return Response(serializer.data)
