from django.db import models

from .publishers import Publisher


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

    class Meta:
        ordering = ['-publication_date', 'title']

    def __str__(self):
        return f'{self.title} ({self.publication_date})'
