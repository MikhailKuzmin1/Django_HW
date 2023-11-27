from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    html = """
    <title>Первый проект</title>
    <body>
        <div>
            <h1>Главная страница</h1>
        </div>
    </body>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <title>О себе</title>
    <body>
        <div>
            <h1>Кузьмин Михаил Сергееевич</h1>
        </div>
    </body>
    """
    return HttpResponse(html)
