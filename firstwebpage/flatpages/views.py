from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")
    # return render(request, 'index.html')
    return render(request, 'static_handler.html')