from django.db import models

# Create your models here.


class PullRequest(models.Model):

    class StatusChoices(models.TextChoices):
        OPEN = 'open','open'
        MERGE = 'merge', 'merge'

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=5, choices=StatusChoices.choices,
    default=StatusChoices.OPEN)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title