from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    Location = models.CharField(max_length=20)
    user_avatar = models.ImageField(upload_to = 'images/')
    Neighbourhood =  models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['username']