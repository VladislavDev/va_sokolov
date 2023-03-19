from django.db import models
from skills.models import HardSkill


class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200,
        default=None,
        blank=True,
        null=True
    )
    preview = models.ImageField(
        upload_to='projects_preview',
        default=None,
        null=True
    )
    skills = models.ManyToManyField(HardSkill)

    def __str__(self):
        return self.name

class Picture(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=400,
        default=None,
        blank=True,
        null=True
    )
