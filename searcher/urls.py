from django.urls import path
from .views import search_view, reload_index
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Hello from Django backend!")),
    path('search/', search_view, name='search'),
    path('reload/', reload_index, name='reload'),
]
