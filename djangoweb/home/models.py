from django.db import models


# Create your models here.


class Service(models.Model):
    title = models.CharField("Title", max_length=100)
    paragraph = models.TextField("Text")
    icon = models.CharField("IconText", max_length=100)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description")
    image = models.ImageField("Image")

    def __str__(self):
        return self.title


class PortfolioModal(models.Model):
    title = models.CharField("Title", max_length=100)
    para1 = models.TextField("Paragraph 1")
    image = models.ImageField("Image", null=True, blank=True)
    para2 = models.TextField("Paragraph 2")
    date = models.DateField("Date")
    client = models.CharField("Client", max_length=100)
    category = models.CharField("Category", max_length=100)
    portfoliomodal = models.OneToOneField(Portfolio, on_delete=models.CASCADE, related_name="portfoliomodal")

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField("Name", max_length=50)
    role = models.CharField("Role", max_length=50)
    image = models.ImageField("Image", null=True, blank=True)

    def __str__(self):
        return self.name
