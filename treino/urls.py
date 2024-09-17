from django.urls import path
from .views import Home, Cadastro, Listar, Editar, delete

app_name = 'treino'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('listar', Listar.as_view(), name='listar'),
    path('editar/<int:pk>', Editar.as_view(), name='editar'),
    path('excluir/<int:pk>', delete, name='excluir'),
]
