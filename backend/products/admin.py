from django.contrib import admin
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name', 'url')
    search_fields = ('name',)
    prepopulated_fields = {"url": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.site_title = "ps4Shop"
admin.site.site_header = "welcome to shop"
