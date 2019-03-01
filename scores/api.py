from rest_framework import serializers, viewsets
from .models import Score
from quizzes.models import Quiz
from teams.models import Team


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('__all__')


class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
