from django.db import models
from uuid import uuid4

# Create your models here.


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name
