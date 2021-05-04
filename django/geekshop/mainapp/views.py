from django.shortcuts import render


def main(request):
    context = {
        'topic': 'Тренды',
        'content': 'НЕУДОБНЫЕ СТУЛЬЯ',
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    links_menu = {'links': ['все', 'офис', 'дом', 'модерн', 'классика']}
    return render(request, 'mainapp/products.html', context=links_menu)


def contact(request):
    return render(request, 'mainapp/contact.html')
