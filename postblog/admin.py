from django.contrib import admin
from postblog.models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Blogpost,BlogpostAdmin)

# Register your models here.
