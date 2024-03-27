from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import PermissionDenied
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .models import Price


class PriceListView(ListView):
    template_name = 'prices/price.list.html'
    model = Price

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['active_paginate_by'] = self.get_paginate_by(self.queryset)
        return context


class PriceDetailView(DetailView):
    template_name = 'prices/price.detail.html'
    pk_field = 'pk'
    model = Price

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        context['request'] = self.request
        context['page_title'] = self.object.title
        return context
    