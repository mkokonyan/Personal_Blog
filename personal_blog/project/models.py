from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    technology = models.CharField(
        max_length=20,
    )
    image = models.URLField(
        max_length=200,
    )

    def __str__(self):
        return f"{self.title}: {self.description}"
