from django.contrib import admin
from blog.models import *
from django import forms
# Register your models here.

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['role']
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','role')
    # list_display_links = ('first_name','last_name')
    pass
    # exclude = ['user']
    # form = UserInfoForm
    # fieldsets = (
    #     (None,{
    #         'fields':('role','user')
    #     }),
    #     ('Advanced options',{
    #         'classes':('wide', 'extrapretty'),
    #         'fields':('article','comment')
    #     }),
    # )
admin.site.register(UserInfo,UserInfoAdmin)

