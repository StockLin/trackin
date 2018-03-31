from django.contrib import admin
from Forum.models import category, forum, message
# Register your models here.

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date')
    ordering = ('-create_date', )


@admin.register(forum)
class forumAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user_id', 'user_name', 'create_date')
    ordering = ('-create_date', )


@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ('forum_id', 'user_id', 'user_name', 'create_date')
    ordering = ('-create_date', )