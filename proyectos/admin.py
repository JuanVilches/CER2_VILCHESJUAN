from django.contrib import admin
from django.contrib.auth.models import User
from .models import Proyecto, UserProfile

class ProyectoAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "estudiante":
            # Filtrar para los estudiantes que no son profesores
            user_ids = UserProfile.objects.filter(es_profesor=False).values_list('user_id', flat=True)
            kwargs["queryset"] = User.objects.filter(id__in=user_ids)
        elif db_field.name == "profesor":
            # Filtrar para los profesores que sí son profesores
            user_ids = UserProfile.objects.filter(es_profesor=True).values_list('user_id', flat=True)
            kwargs["queryset"] = User.objects.filter(id__in=user_ids)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(UserProfile)
