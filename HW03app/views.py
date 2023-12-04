from django.http import HttpResponse
from django.shortcuts import render
from HW02app.models import Order, Product
from datetime import datetime, timedelta

# Create your views here.

def order_week(request):
    data = Product.objects.filter(date_update__gte=datetime.now()-timedelta(days=7))
    res = [i.name for i in data]
    context = {'value': res}
    return render(request, 'template/order.html', context=context)

def order_month(request):
    data = Product.objects.filter(date_update__gte=datetime.now()-timedelta(days=30))
    res = [i.name for i in data]
    context = {'value': res}
    return render(request, 'template/order.html', context=context)

def order_year(request):
    data = Product.objects.filter(date_update__gte=datetime.now()-timedelta(days=365))
    res = [i.name for i in data]
    context = {'value': res}
    return render(request, 'template/order.html', context=context)