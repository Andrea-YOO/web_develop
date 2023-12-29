from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # '/' 주소에서 index 뷰로 라우팅
    path('about/', views.about, name='about'),  # '/about/' 주소에서 about 뷰로 라우팅
]