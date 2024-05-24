from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=126)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
