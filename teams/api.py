from rest_framework import serializers, viewsets
from .models import Team
from scores.api import ScoreSerializer
from django.db.models.functions import Cast
from django.db.models import Avg, Q, FloatField, Sum, Count, Max


class TeamSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    average_score = serializers.FloatField()
    average_r1_score = serializers.FloatField()
    average_r2_score = serializers.FloatField()
    average_r3_score = serializers.FloatField()
    average_r4_score = serializers.FloatField()
    average_r5_score = serializers.FloatField()
    average_r6_score = serializers.FloatField()
    average_r7_score = serializers.FloatField()
    average_r8_score = serializers.FloatField()
    games_played = serializers.IntegerField()
    average_percent_correct = serializers.FloatField(min_value=0.0000001)
    high_score = serializers.IntegerField()

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
        total_points_scored = Cast(Sum(
            'scores__total_points_scored'), FloatField())
        total_points = Cast(Sum('scores__quiz__total_points'), FloatField())
        average = (total_points_scored / total_points) * 100
        return Team.objects.annotate(
            average_score=Avg('scores__total_points_scored'),
            average_r1_score=Avg('scores__r1_points_scored'),
            average_r2_score=Avg('scores__r2_points_scored'),
            average_r3_score=Avg('scores__r3_points_scored'),
            average_r4_score=Avg('scores__r4_points_scored'),
            average_r5_score=Avg('scores__r5_points_scored'),
            average_r6_score=Avg('scores__r6_points_scored'),
            average_r7_score=Avg('scores__r7_points_scored'),
            average_r8_score=Avg('scores__r8_points_scored'),
            games_played=Count('scores__quiz'),
            average_percent_correct=average,
            high_score=Max('scores__total_points_scored')
        ).order_by('team_name')


# class LeaderboardViewSet(viewsets.ModelViewSet):
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()

#     def get_queryset(self):
#         total_points_scored = Cast(Sum(
#             'scores__total_points_scored'), FloatField())
#         total_points = Cast(Sum('scores__quiz__total_points'), FloatField())
#         average = (total_points_scored / total_points) * 100
#         return Team.objects.annotate(
#             average_score=Avg('scores__total_points_scored'),
#             games_played=Count('scores__quiz'),
#             average_percent_correct=average
#         ).filter(Q(games_played__gt=2)).order_by('-average_score')
