# Vai controlar apenas rotas relacionadas ao app notes.

from django.urls import path

from . import views

# Quando a rota vazia ('') for acessada, ele deve utilizar a função views.index 
# para construir a resposta.
urlpatterns = [
    path('', views.index, name='index'),
]