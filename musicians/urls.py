# musicians/urls.py
from django.urls import path
from .views import musician_list, musician_detail, musician_create, musician_edit, musician_delete

urlpatterns = [
    path('', musician_list, name='musician_list'),
    path('<int:pk>/', musician_detail, name='musician_detail'),
    path('new/', musician_create, name='musician_create'),
    path('<int:pk>/edit/', musician_edit, name='musician_edit'),
    path('<int:pk>/delete/', musician_delete, name='musician_delete'),
]
