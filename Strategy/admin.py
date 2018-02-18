from django.contrib import admin
from Strategy.models import strategy
# Register your models here.

# @admin.register(s_category)
# class categoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'create_date', 'modify_date')
#     ordering = ('-create_date',)


# @admin.register(s_level)
# class levelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'create_date', 'modify_date')
#     ordering = ('-create_date',)


@admin.register(strategy)
class strategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'create_date')
    ordering = ('-create_date',)

