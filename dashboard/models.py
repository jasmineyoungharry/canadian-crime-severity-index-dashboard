from django.db import models


class CrimeRecord(models.Model):
    province_or_territory = models.CharField(max_length=100)
    year = models.IntegerField()
    metric = models.CharField(max_length=200)
    value = models.FloatField()

    def __str__(self):
        return f"{self.province_or_territory} | {self.year} | {self.metric}"