from django.urls import path

from . import views

app_name = 'online_test'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    path('test/judge/', views.judge, name='judge')
]
