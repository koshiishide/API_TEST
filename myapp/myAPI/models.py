from django.db import models
#一旦　データベース作成


class User(models.Model):
    name = models.CharField(max_length=32)
    chat = models.CharField(max_length=32)