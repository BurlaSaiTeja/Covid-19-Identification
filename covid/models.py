from django.db import models


class TestStatus(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Patient Name")
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
