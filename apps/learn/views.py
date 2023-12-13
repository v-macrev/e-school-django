# Módulos de Bibliotecas Padrão
from datetime import datetime
import io, json, locale

# Módulos de Biblioteca Django
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import connections


@login_required(login_url="/bem-vindo/")
def index(request):
    # Pass data into context
    context = {'segment': 'index'}

    # Render the template with the data
    return render(request, 'learn/index.html', context)

@login_required(login_url="/bem-vindo/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
