from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=150)
    code = models.IntegerField()

    def __str__(self):
        return self.username
