from django.shortcuts import render

from .models import ProductCategory, Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
        'topic': 'Тренды',
        'content': 'НЕУДОБНЫЕ СТУЛЬЯ',
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    links_menu = {'links': ['все', 'офис', 'дом', 'модерн', 'классика']}
    return render(request, 'mainapp/products.html', context=links_menu)


def contact(request):
    return render(request, 'mainapp/contact.html')
