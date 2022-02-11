from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class PhotoHome(ListView):
    model = Photo
    template_name = 'main/index.html'
    context_object_name = 'album'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Photo.objects.filter(is_published=True)


# def show_post(request, post_slug):
#    post = get_object_or_404(Photo, slug=post_slug)
#
#    context = {
#        'post': post,
#        'title': post.title,
#        'cat_selected': post.cat_id,
#    }
#
#    return render(request, 'main/post.html', context=context)

class ShowPost(DetailView):
    model = Photo
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отображение фото'
        return context


# def index(request):
#    album = Photo.objects.all()
#    context = {
#        'title': 'Главная страница',
#        'album': album,
#        'cat_selected': 0,
#    }
#
#    return render(request, 'main/index.html', context=context)


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление картины'
        return context


# def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AddPostForm
#    return render(request, 'main/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return render(request, 'main/about.html', {'title': 'Как нам написать?'})


def login(request):
    return render(request, "main/login.html", {'title': 'Авторизация в системе'})


def about(request):
    return render(request, 'main/about.html', {'title': 'Об авторе'})


def PageNotFound(request, exception):
    text = '''
    Данная страница не найдена, обратитесь в техподдержку
    '''
    return render(request, 'main/error404.html', {'title': 'Страница не найдена', 'text': text})


# def show_category(request, cat_id):
#    album = Photo.objects.filter(cat_id=cat_id)
#
#    if len(album) == 0:
#        raise Http404()
#
#    context = {
#        'title': f'Отображение картин по рубрикам',
#        'album': album,
#        'cat_selected': cat_id,
#    }
#
#    return render(request, 'main/index.html', context=context)


class PhotoCategory(ListView):
    model = Photo
    template_name = 'main/index.html'
    context_object_name = 'album'
    allow_empty = False

    def get_queryset(self):
        return Photo.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['album'][0].cat)
        context['cat_selected'] = context['album'][0].cat_id
        return context
