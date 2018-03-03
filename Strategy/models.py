from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
# Create your models here.

# # Strategies category definition
# class s_category(models.Model):
#     name = models.CharField(max_length=100)
#     create_date = models.DateTimeField(auto_now_add=True)
#     modify_date = models.DateTimeField(default=None, null=True, blank=True)

#     def __str__(self):
#         return self.name


# # Strategies level definition
# class s_level(models.Model):
#     name = models.CharField(max_length=100)
#     create_date = models.DateTimeField(auto_now_add=True)
#     modify_date = models.DateTimeField(default=None, null=True, blank=True)

#     def __str__(self):
#         return self.name
# path generations with Strategy setting
def file_path(instance, filename):
    path = 'strategies/{}/{}/{}'.format(instance.category, instance.level, filename)
    return path

# Strategies model fields definition
class strategy(models.Model):
    CATEGORY_SELECTIONS = (
        ('bull', '多頭'),
        ('bear', '空頭'),
    )

    LEVEL_SELECTIONS = (
        ('normal', '普通'),
        ('golden', '黃金'),
        ('platinum', '白金'),
        ('diamond', '鑽石'),
    )
    category = models.CharField(max_length=255, choices=CATEGORY_SELECTIONS, verbose_name='多空頭類別')
    level = models.CharField(max_length=255, choices=LEVEL_SELECTIONS, verbose_name='會員等級')
    name = models.CharField(max_length=255, verbose_name='策略名稱')
    description = models.TextField(verbose_name='策略敘述')
    standard = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='標準差')
    avg_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='平均報酬率')
    total_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='總報酬率')
    max_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='最高報酬率')
    total_transa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='總交易次數')
    max_loss = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='最大虧損率')
    win_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='勝率')
    files_dir = models.FileField(upload_to=file_path, verbose_name='檔案上傳')
    like = models.PositiveIntegerField(default=0, verbose_name='喜歡數')
    create_date = models.DateTimeField(auto_now_add = True, verbose_name='上傳日期')
    modify_date = models.DateTimeField(null = True, blank = True, verbose_name='修改日期')

    def __str__(self):
        return self.name

# after strategy models objects are deleted, signal are triggered
@receiver(post_delete, sender=strategy)
def strategy_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.files_dir.delete(False)



# def file_path(instance):
#     # files diratory selections
#     FILES_DIR_CHOICES = (
#         ('strategies/bull/normal', '多頭-普通-路徑'),
#         ('strategies/bull/golden', '多頭-黃金-路徑'),
#         ('strategies/bull/platinum', '多頭-白金-路徑'),
#         ('strategies/bull/diamond', '多頭-鑽石-路徑'),
#         ('strategies/bear/normal', '空頭-普通-路徑'),
#         ('strategies/bear/golden', '空頭-黃金-路徑'),
#         ('strategies/bear/platinum', '空頭-白金-路徑'),
#         ('strategies/bear/diamond', '空頭-鑽石-路徑'),
#     )