from django.contrib import admin
from Users.models import Profile
# Register your models here.

# user profile class definition
@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'balance', 'remain_day')
    ordering = ('-signup_date',)

