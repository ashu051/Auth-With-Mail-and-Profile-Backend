from django.contrib import admin
from .models import User , Mail
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','message')
admin.site.register(User,UserAdmin)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id','message','email')
admin.site.register(Mail,MailAdmin)