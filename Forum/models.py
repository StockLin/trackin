from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name



#討論文章models
class forum(models.Model):
    category = models.ForeignKey('category', on_delete = models.CASCADE)
    user_id = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    img_url = models.URLField(max_length=255, null=True, blank=True)
    like_num = models.PositiveIntegerField(default = 0)
    unlike_num = models.PositiveIntegerField(default = 0)
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title


# 訊息留言models
class message(models.Model):
    forum_id = models.ForeignKey('forum', on_delete = models.CASCADE)
    user_id = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)
    img_url = models.URLField(max_length=255, null=True, blank=True)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True, blank = True)
