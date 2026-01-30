from django.contrib import admin
from rango.models import Category, Page

# Admin configuration for Page
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
