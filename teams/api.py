import io
from rest_framework.parsers import JSONParser
from rest_framework import serializers, viewsets
from .models import Team
from scores.api import ScoreSerializer


class TeamSerializer(serializers.ModelSerializer):
    # scores = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'scores', 'average_score')

    def get_average_score(self, object):

        return object.team_name


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
