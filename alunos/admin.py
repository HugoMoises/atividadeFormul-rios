from django.contrib import admin
from . models import Aluno
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'curso')
    search_fields = ('nome', 'email', 'curso')
    list_filter = ('nome','email', 'curso')