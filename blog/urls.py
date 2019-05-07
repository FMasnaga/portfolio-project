
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:id>',views.detail, name='detail'),
]