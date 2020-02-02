from django.db import models
# from django.utils import timezone

class Author(models.Model):
    name=models.CharField(max_length=42,primary_key=True,verbose_name='name')

# Create your models here.
class New(models.Model):
    text=models.CharField(max_length=400)
    dt= models.DateField()
    autor_id=models.ForeignKey(Author, on_delete=models.CASCADE)

