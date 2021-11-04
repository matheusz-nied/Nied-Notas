from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cria/nota', views.cria_nota, name='cria_nota'),
    path('delete/<int:nota_id>', views.delete_nota, name='delete_nota'),
    path('edit/nota', views.edit_nota, name='edit_nota'),

]