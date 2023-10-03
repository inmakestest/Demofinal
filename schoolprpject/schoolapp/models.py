from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dec=models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
