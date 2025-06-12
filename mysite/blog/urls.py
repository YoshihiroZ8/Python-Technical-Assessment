from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('admin/', amin.site.urls),
    path('', include('blog.urls')),
]