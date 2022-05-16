from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfilreInfo(models.Model):
    user = models.OneToOneField(User)
    protfolio_site = mdoels.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank= true)
    def __str__(self):
        return self.user.username
