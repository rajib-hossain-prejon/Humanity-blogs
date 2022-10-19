from django.contrib import admin
from . import models
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse

# Register your models here.

class PostsImageInline(admin.TabularInline):
    model = models.PostsImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" '  )
        return ''


@admin.register(models.Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['blogger', 'description','date']
    list_per_page = 10
    inlines = [PostsImageInline]

    class Media:
        css = {
            'all': ['blogs/styles.css']
        }

class BloggersImageInline(admin.TabularInline):
    model = models.BloggersImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" '  )
        return ''

@admin.register(models.Blogger)
class BloggerAdmin(admin.ModelAdmin):
 list_display = ['first_name', 'last_name', 'membership','birth_date']
 list_editable = ['membership']
 list_per_page = 10
 list_select_related = ['user']
 ordering =['user__first_name', 'user__last_name']
 search_fields = ['first_name__istartswith']
 
 inlines = [BloggersImageInline]

 class Media:
        css = {
            'all': ['blogs/styles.css']
        }

