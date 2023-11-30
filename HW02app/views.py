from django.http import HttpResponse
from django.shortcuts import render
from.models import Client, Order, Product

# Create your views here.

def index(request):
    return HttpResponse('Hello, world!')


def create_client(request):
    for i in range(11):
        client = Client(
                        name=f'name{i}',
                        email=f'mail@mail{i}.com',
                        phone=f'{i}911111111',
                        adress=f'Home №{i}'
                        )
        client.save()
    return HttpResponse('Create 10 clients!')

def create_product(request):
    for i in range(11):
        product = Product(
                        name=f'name{i}',
                        about=f'product - {i}',
                        price=f'{i}.99',
                        count=f'{i}'
                        )
        product.save()
    return HttpResponse('Create 10 products!')

def create_order(request):
    for i in range(11):
        order = Order(total_price=f'{i}00', customer_id='1')
        order.save()
    return HttpResponse('Create 10 orders!')
