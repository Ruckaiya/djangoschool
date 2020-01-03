from django.db import models

# Create your models here.
class Calender(models.Model):
    year = models.CharField(max_length=10)
    pdf = models.FileField(upload_to='files')

    def __str__(self):
        return self.year
    
  