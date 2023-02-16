from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=130)
    password = models.CharField(max_length=130)

class Login(models.Model):
    email = models.EmailField(max_length=130)
    password = models.CharField(max_length=130)


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title