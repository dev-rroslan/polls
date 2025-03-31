from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
  
  return render(request, 'pages/index.html')


def example_endpoint(request):
    return JsonResponse({"message": "Hello from HTMX!"})