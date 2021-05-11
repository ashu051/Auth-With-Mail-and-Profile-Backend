from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Mail(models.Model):
    email=models.CharField(max_length=50)
    message = models.CharField(max_length=50)
class Friend_request(models.Model):
    friends= models.ManyToManyField(User,blank=True,max_length=40,null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='to_user')