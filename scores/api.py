from rest_framework import serializers, viewsets
from .models import Score
from quizzes.models import Quiz
# from teams.api import TeamSerializer


class ScoreSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField(read_only=True)
    quiz = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Score
        fields = ('__all__')


class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
