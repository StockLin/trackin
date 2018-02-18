from django.db import models

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
    category = models.CharField(max_length=255, choices=CATEGORY_SELECTIONS)
    level = models.CharField(max_length=255, choices=LEVEL_SELECTIONS)
    name = models.CharField(max_length=255)
    description = models.TextField()
    standard = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    avg_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_return = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_transa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_loss = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    win_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    files_dir = models.FileField(upload_to=file_path)
    like = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name



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