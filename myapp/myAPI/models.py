from django.db import models
#一旦　データベース作成


class User(models.Model):
    user_name = models.CharField(max_length=32)
    text = models.CharField(max_length=32)
