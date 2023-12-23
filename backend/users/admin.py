from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.safestring import mark_safe


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'last_login', 'is_staff')
    list_display_links = ('id', 'username')
    search_fields = ('email',)
    readonly_fields = ("get_image",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Информация о полльзователе"), {"fields": ("first_name", "last_name", "photo", "get_image", "date_birth")}),

        (("Важные даты"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
            },
        ),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110"')


admin.site.register(User, CustomUserAdmin)

admin.site.site_title = "ps4Shop"
admin.site.site_header = "welcome to shop"
