from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

