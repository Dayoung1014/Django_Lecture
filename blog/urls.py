from django.urls import path
from . import views

urlpatterns = [# 서버IP/blog
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>', views.tag_page),  # 서버IP/blog/tag/slug
    path('category/<str:slug>', views.category_page),  # 서버IP/blog/category/slug
    # path('<int:pk>/', views.singel_post_page),  # 서버IP/blog/pk
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index),  # path(''. ) 현재 위치가 서버IP/blog
    path('', views.PostList.as_view()), #PostList (모델이름 + List)
]