from django.db import models

# Create your models here.
class Car(models.Model):
  price = models.CharField(max_length=50)
  year = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  ext_color = models.CharField(max_length=50)
  int_color = models.CharField(max_length=50)
  transmission = models.CharField(max_length=50)
  contact = models.CharField(max_length=50)

  def __str__(self):
    return self.model