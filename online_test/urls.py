from django.urls import path

from . import views

app_name = 'online_test'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    path('test/submit_answer/', views.submit_answer, name='judge'),
    path('test/problem_bank/', views.ProblemBank.as_view(), name='problem_bank'),
]
