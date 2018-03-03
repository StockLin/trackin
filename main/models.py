from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length = 255, verbose_name='客戶名稱')
    email = models.EmailField(max_length=254, verbose_name='客戶信箱')
    contents = models.TextField(verbose_name='內容')
    send_date = models.DateTimeField(auto_now_add=True, verbose_name='發送日期')

    def __str__(self):
        return self.name