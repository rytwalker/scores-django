from rest_framework import serializers, viewsets
from .models import Team
from scores.api import ScoreSerializer


class TeamSerializer(serializers.ModelSerializer):
    # scores = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'scores')


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
