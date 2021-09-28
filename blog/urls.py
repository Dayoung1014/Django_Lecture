from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # path(''. ) 현재 위치가 서버IP/blog
    path('<int:pk>/', views.singel_post_page),  # 서버IP/blog/pk
]