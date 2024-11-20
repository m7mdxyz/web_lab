from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    
class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city
    
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    
class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)


class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

