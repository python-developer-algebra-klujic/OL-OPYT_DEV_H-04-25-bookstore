from django.db import models


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.name
