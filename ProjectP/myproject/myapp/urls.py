from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add/', views.add_person, name='add_person'),
    path('edit/<int:id>/', views.edit_person, name='edit_person'),
    path('delete/<int:id>/', views.delete_person, name='delete_person'),
]
