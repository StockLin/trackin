from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# user models definition

class Profile(models.Model):
    STATUS_CHOICES = (
        (0, '一般會員'),
        (1, '黃金會員'),
        (2, '白金會員'),
        (3, '鑽石會員'),
    )
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    )
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=0, choices=STATUS_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_day = models.DateTimeField(auto_now_add=True)
    end_day = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, default='O', null=True, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=255, default=None, null=True, blank=True)
    remain_day = models.PositiveIntegerField(default=0)
    signup_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, default=None)