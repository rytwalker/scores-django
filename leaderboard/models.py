from django.db import models
from uuid import uuid4


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(auto_now=True)
    total_points = models.PositiveSmallIntegerField(default=96)
    r1_points = models.PositiveSmallIntegerField(default=8)
    r2_points = models.PositiveSmallIntegerField(default=16)
    r3_points = models.PositiveSmallIntegerField(default=8)
    r4_points = models.PositiveSmallIntegerField(default=8)
    r5_points = models.PositiveSmallIntegerField(default=8)
    r6_points = models.PositiveSmallIntegerField(default=8)
    r7_points = models.PositiveSmallIntegerField(default=8)
    r8_points = models.PositiveSmallIntegerField(default=16)
    r1_category = models.CharField(max_length=200)
    r2_category = models.CharField(max_length=200)
    r3_category = models.CharField(max_length=200)
    r4_category = models.CharField(max_length=200)
    r5_category = models.CharField(max_length=200)
    r6_category = models.CharField(max_length=200)
    r7_category = models.CharField(max_length=200)
    r8_category = models.CharField(default='random', max_length=200)

    def __str__(self):
        unformatted_date = str(self.created_at).split(' ')[0]
        split_date = unformatted_date.split('-')
        date = split_date[1] + '-' + split_date[2] + '-' + split_date[0]
        return date


class Leaderboard(models.Model):
