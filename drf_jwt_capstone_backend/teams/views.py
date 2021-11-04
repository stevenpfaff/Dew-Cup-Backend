from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Team
from .serializers import TeamSerialzer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_teams(request):
    teams = Team.objects.all()
    serializer = TeamSerialzer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_team(request):
    if request.method == 'POST':
        serializer = TeamSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        teams = Team.objects.filter(team_id=request.user.id)
        serializer = TeamSerialzer(teams, many=True)
        return Response(serializer.data)
