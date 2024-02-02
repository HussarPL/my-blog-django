from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250) #pole tytuł
    content = models.TextField(default='') #pole zawartość
    year = models.PositiveIntegerField(default=2024) #pole rok
    imgThumb = models.ImageField(upload_to='images', null=True, blank=True) #obrazek


    def __str__(self):
        return self.title_with_year()


    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
