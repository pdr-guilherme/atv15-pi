from django.contrib import admin

from acervo.models import Autor, Livro


class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    search_fields = ("nome", "email")


class LivroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "editora")
    search_fields = ("titulo", "autor", "resumo")
    list_filter = ("editora",)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro, LivroAdmin)
