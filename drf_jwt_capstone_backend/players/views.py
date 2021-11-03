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

class PlayerList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerialzer(players, many=True)
        return Response(serializer.data)