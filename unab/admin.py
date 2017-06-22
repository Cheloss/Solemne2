# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from unab.models import Movie, Category, Noticia
from sorl.thumbnail.admin import AdminImageMixin

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','anio','sort_order','id')
    list_filter = ('anio',)
    list_search = ('name','anio')
class Noticia(admin.ModelAdmin):
    list_display = ('titulo','category','sort_order','id')
    list_filter = ('created',)
    list_search = ('titulo',)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie,MovieAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Noticia,NoticiaAdmin)