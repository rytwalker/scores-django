from rest_framework import serializers, viewsets
from .models import Quiz
from scores.api import ScoreSerializer


class QuizSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('__all__')


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all().order_by('-created_at')
