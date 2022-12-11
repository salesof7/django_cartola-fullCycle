from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    initial_price = models.FloatField()

    def __str__(self):
        return self.name
