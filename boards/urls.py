from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
]
