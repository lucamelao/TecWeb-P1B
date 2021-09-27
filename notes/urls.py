# Vai controlar apenas rotas relacionadas ao app notes.

from django.urls import path

from . import views

# Quando a rota vazia ('') for acessada, ele deve utilizar a função views.index 
# para construir a resposta. A mesma lógica se aplica às outras rotas.
urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.remove_note, name='remove_note'),
    path('update', views.update_note, name='update_note'),
    path('all_tags', views.list_tags, name='list_tags'),
    path('notes_per_tag', views.group_per_tag, name='group_per_tag'),
]


# ---- Comandos úteis para rodar o projeto ----

# COM O DOCKER ABERTO
# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=insper -d -p 5432:5432 -v C:\Users\lucam\docker\volumes\postgres:/var/lib/postgresql/data postgres
# python manage.py runserver
# env\Scripts\activate.bat
# c:/Users/lucam/Documents/INSPER/4º SEMESTRE/TecWeb-P1B

# ---------------------------------------------