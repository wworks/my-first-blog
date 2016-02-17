from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    naam = models.TextField(null=False)
    regid = models.TextField(null = True)
    klas = models.CharField(max_length=5,null=True)
    betaald = models.BooleanField(default=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.naam + " " + self.klas