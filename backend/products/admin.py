from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name', 'url')
    search_fields = ('name',)
    prepopulated_fields = {"url": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "aviable", "is_published",)
    list_filter = ("categories", "title")
    prepopulated_fields = {"url": ("title",)}
    search_fields = ("title",)
    # inlines = [MovieShotsInline, ReviewInline, ]

    save_on_top = True
    save_as = True
    list_editable = ("is_published",)
    actions = ['unpublish', 'publish']

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.poster.url} width="150" height="120">')

    def unpublish(self, request, queryset):
        """change publication"""
        row_update = queryset.update(is_published=True)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """publicate"""
        row_update = queryset.update(is_published=False)
        if row_update == 1:
            message_bit = '1 запись обновлена'
        else:
            message_bit = f'{row_update} записей обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    publish.allowed_permissions = ('change',)

















admin.site.register(Category, CategoryAdmin)
admin.site.site_title = "ps4Shop"
admin.site.site_header = "welcome to shop"
