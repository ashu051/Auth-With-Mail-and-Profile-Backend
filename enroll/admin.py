from django.contrib import admin
from .models import User , Mail ,Friend_request
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','message')
admin.site.register(User,UserAdmin)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id','message','email')
admin.site.register(Mail,MailAdmin)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id','from_user','to_user')
admin.site.register(Friend_request,FriendAdmin)