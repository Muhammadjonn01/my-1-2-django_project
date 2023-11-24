from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "footer_header.html"


class Partfolio(TemplateView):
    template_name = "partfolio.html"

    
class About(TemplateView):
    template_name = "about.html"
