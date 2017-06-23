# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unab.models import Noticia, Foto
from django.shortcuts import render, get_object_or_404
from unab.forms import NoticiaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

im = get_thumbnail(Foto.image, '500x300', crop='center', quality=99)

def noticia_list(request):
    data = {}

    data['object_list'] = Noticia.objects.all().order_by('-created')


    template_name = 'noticia/noticia_list.html'
    return render(request, template_name, data)

def noticia_update(request, pk) :
    data = {}

    data['object_list'] = Noticia.objects.filter(pk=pk)
    template_name = 'noticia/noticia_detalle.html'
    return render(request, template_name, data)


