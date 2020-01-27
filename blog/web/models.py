from django.db import models
class User(models.model):
    first_name=models.charfeild(max_length=128)
    last_name=models.charfeild(max_length=128)
    password=models PasswordField(max_length=254,unique=True)
# Create your models here.
