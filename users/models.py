from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    image = models.ImageField(default='profilepic.jpg',
                              upload_to='profile_pictures')
    number = models.IntegerField(default=99)
    coupons = models.CharField(max_length=100, blank=True)
    wishlist = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


class Coupons(models.Model):
    coupon_code = models.CharField(max_length=10)
    coupon_desc = models.CharField(max_length=100)
    discount = models.IntegerField()
    issue_date = models.DateField()
    expire_date = models.DateField()
