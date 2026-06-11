from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()



class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    phone = models.IntegerField()


class Car(models.Model):
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    
    



def __str__(self):           #constructor
    return self.name


