from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
  
  return render(request, 'template/main.html')

def about(request):
    context = {'name': 'mikhail'}
    return render(request, 'template/index.html', context=context)
