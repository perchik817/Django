from django.db import models

# Create your models here.
class Cars(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    color = models.CharField(max_length=60)
    created_year = models.DateField()
    ratings = models.IntegerField(max_length=10, null=True)
    #при изменении модельки надо указать null=True

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    site = models.URLField(null = True)
    
    def __str__(self):
        return self.name
