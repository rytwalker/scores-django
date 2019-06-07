import io
from rest_framework.parsers import JSONParser
from rest_framework import serializers, viewsets
from .models import Team
from scores.api import ScoreSerializer
from django.db.models.functions import Cast
from django.db.models import Avg, Q, FloatField, Sum, Count
# from django.db import models


class TeamSerializer(serializers.ModelSerializer):
    scores = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # scores = ScoreSerializer(many=True, read_only=True)
    average_score = serializers.FloatField()
    games_played = serializers.IntegerField()
    # average_percent_correct = serializers.DecimalField(
    #     max_digits=5, decimal_places=5, coerce_to_string=False)
    average_percent_correct = serializers.FloatField(min_value=0.0000001)

    class Meta:
        model = Team
        fields = "__all__"

    def get_average_score(self, object):
        print(object.scores__score)
        return object.team_name


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return Team.objects.annotate(
            average_score=Avg('scores__total_points_scored'),
            games_played=Count('scores__quiz')
        )


class LeaderboardViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        total_points_scored = Cast(Sum(
            'scores__total_points_scored'), FloatField())
        total_points = Cast(Sum('scores__quiz__total_points'), FloatField())
        # print(total_points)
        average = (total_points_scored / total_points) * 100
        return Team.objects.annotate(
            average_score=Avg('scores__total_points_scored'),
            games_played=Count('scores__quiz'),
            average_percent_correct=average
        ).filter(Q(games_played__gt=2)).order_by('-average_score')
