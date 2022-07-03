from django.db import models

# Create your models here.
class Topics(models.Model):
    topic_name=models.CharField(max_length=100, primary_key=True)

class Webpages(models.Model):
    topic_name=models.ForeignKey(Topics, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    name=models.URLField()


class AccessRecords(models.Model):
    name=models.ForeignKey(Webpages, on_delete=models.CASCADE)
    date=models.DateField()
