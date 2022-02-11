from django import template
from main.models import *


register = template.Library()


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('main/menu.html')
def show_menu():
    menu = [{'title': 'Добавить картину', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'О нас', 'url_name': 'about'},
            {'title': 'Войти', 'url_name': 'login'},
            ]

    return {'menu': menu}
