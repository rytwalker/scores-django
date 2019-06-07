from django.db import models
from uuid import uuid4
from teams.models import Team
from quizzes.models import Quiz


class Score(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team = models.ForeignKey(
        Team, related_name='scores', on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, related_name='scores', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(auto_now=True)
    total_points_scored = models.PositiveSmallIntegerField(default=0)
    r1_points_scored = models.PositiveSmallIntegerField(default=0)
    r2_points_scored = models.PositiveSmallIntegerField(default=0)
    r3_points_scored = models.PositiveSmallIntegerField(default=0)
    r4_points_scored = models.PositiveSmallIntegerField(default=0)
    r5_points_scored = models.PositiveSmallIntegerField(default=0)
    r6_points_scored = models.PositiveSmallIntegerField(default=0)
    r7_points_scored = models.PositiveSmallIntegerField(default=0)
    r8_points_scored = models.PositiveSmallIntegerField(default=0)
    round_jokered = models.PositiveSmallIntegerField(default=8)
    won_tiebreaker = models.BooleanField(blank=True)

    def __str__(self):
        return f"{str(self.team)} on {str(self.quiz)}"
