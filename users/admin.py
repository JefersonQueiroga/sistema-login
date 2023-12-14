from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    # Defina os fieldsets para adicionar/editar formas
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("username","cpf", "sexo")}),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = ("email", "username", "is_staff")
    search_fields = ("email", "username")
