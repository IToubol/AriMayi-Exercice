from django.db import models


# Create your models here.


class Candidates(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    registred_on = models.DateTimeField(auto_now_add=True)
    hard_skills = []

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"