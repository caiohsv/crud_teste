from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('addlivro/', views.addlivro, name='addlivro'),
   path('editlivro/<int:id>', views.editlivro, name='editlivro'),
   path('deletepro/<int:id>', views.deletelivro, name='deletelivro')
   
]
