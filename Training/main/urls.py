from django.urls import path

from .views import *

urlpatterns = [
    path('', PhotoHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('photo/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', PhotoCategory.as_view(), name='category')
]
