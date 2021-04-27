from django.db import models

# Create your models here.


class Service(models.Model):
    image = models.ImageField("Foto", null=True, blank=True)
    title = models.CharField("Title", max_length=100)
    paragraph = models.TextField("Text")

    def __str__(self):
        return self.title
