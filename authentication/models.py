from django.db import models

# Create your models here.\
class Skills(models.Model):
    name=models.CharField(max_length=50)
    

class  Freelancer(models.Model):
    email= models.EmailField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    description=models.CharField(max_length=1000, null=True)
    profile_picture=models.ImageField(null=True)
    skills=models.ManyToManyField(Skills,blank=True)
    certificates=models.FileField(null=True)
    contact_number=models.CharField(max_length=50, blank= True)
    

class Experience(models.Model):
    years=models.IntegerField()
    s=models.ForeignKey(Skills,on_delete=models.CASCADE)


class Company(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField()
    role=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    profile_picture=models.ImageField()
    address=models.CharField(max_length=200)
    contact_number=models.IntegerField(blank=True, null=True)

    



