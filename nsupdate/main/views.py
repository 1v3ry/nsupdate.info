# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponse
import json

class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['nav_home'] = True
        return context

def MyIpView(request):
	return HttpResponse(json.dumps({'ip':request.META['REMOTE_ADDR']}), content_type="application/json")