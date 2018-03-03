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
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, verbose_name='會員')
    status = models.PositiveIntegerField(default=0, choices=STATUS_CHOICES, verbose_name='會員等級')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='餘額')
    start_day = models.DateTimeField(auto_now_add=True, verbose_name='開始日期')
    end_day = models.DateTimeField(auto_now_add=True, verbose_name='到期日期')
    gender = models.CharField(max_length=10, default='O', null=True, choices=GENDER_CHOICES, verbose_name='性別')
    phone = models.CharField(max_length=255, default=None, null=True, blank=True, verbose_name='電話')
    remain_day = models.PositiveIntegerField(default=0, verbose_name='剩餘天數')
    signup_date = models.DateTimeField(auto_now_add=True, verbose_name='註冊日期')
    # modify_date = models.DateTimeField(null=True, default=None)