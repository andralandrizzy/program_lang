from django.contrib import admin
from . models import Articles
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('title',)
    list_per_page = 15
    

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Articles, ArticlesAdmin)