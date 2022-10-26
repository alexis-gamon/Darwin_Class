from django.contrib import admin
from .models import Curso, Comentario, Lenguaje

#class ComentarioInline(admin.StackedInline):
#    model = Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario

class CursoAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline
    ]
  


admin.site.register(Curso, CursoAdmin)
admin.site.register(Lenguaje)
admin.site.register(Comentario)