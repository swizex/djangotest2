from django.http import HttpResponse
from django.views.generic import View


def home(request):
    html = "<h1> TESTING </h1>"
    return HttpResponse(html)