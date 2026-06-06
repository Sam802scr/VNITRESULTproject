from django.db import models

class ResultColumn(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)

    class Meta:
        unique_together = (('id', 'course',),) ##checkthis!!!
# Create your models here.
