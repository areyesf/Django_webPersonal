from django.contrib import admin
from .models import Projecto

# Register your models here.
class ProjectoAdmin(admin.ModelAdmin):
    readonly_fields=("fch_creado", "fch_mod")


admin.site.register(Projecto, ProjectoAdmin)

