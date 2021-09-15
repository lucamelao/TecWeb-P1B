"""getit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# Faz a associação com o notes/urls.py, pois este getit/urls.py é na verdade
# o responsável pelas rotas 
from django.urls import include, path

# A função include fala para o Django incluir na rota especificada
# (no caso a rota vazia '') todas as rotas definidas no arquivo notes/urls.py. 
# Ao receber uma requisição, o Django percorre a lista urlpatterns do arquivo getit/urls.py 
# procurando a primeira rota que seja igual à rota solicitada. 

# Por esse motivo, a ordem dos elementos da lista urlpatterns é muito importante: 
# em caso de duas rotas com o mesmo nome, será escolhida a que ocorrer primeiro.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]