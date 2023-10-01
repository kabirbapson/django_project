from django.db import models

# Create your models here.
class Collections(models.Model):
    col_name = models.CharField(max_length=100)
    col_description = models.CharField(max_length=500)
    col_cover = models.CharField(max_length=1000, default='img')

    def __str__(self):
        return self.col_name

class Piece(models.Model):
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    p_title = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100, default='article')
    p_artist = models.CharField(max_length=100)
    p_year = models.IntegerField()
    p_cover = models.CharField(max_length=1000, default='img')
    
    def __str__(self):
        return self.p_title