from django.db import models
class fare(models.Model):
    trainNum = models.PositiveIntegerField(primary_key=True)
    OrgCity = models.CharField(max_length=250)
    DesCity = models.CharField(max_length=250)
    TrainFare = models.PositiveIntegerField()


# Create your models here.
