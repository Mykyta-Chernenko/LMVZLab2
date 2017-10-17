from django.db import models
class Proportion(models.Model):
    weight = models.SmallIntegerField()
    sex = models.CharField(max_length=10)
    height =models.SmallIntegerField()

    class Meta:
        ordering = ['height','sex']
        unique_together =['height','sex']




