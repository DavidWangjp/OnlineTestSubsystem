from django.urls import path

from . import views

app_name = 'online_test'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    path('test/submit_answer/', views.submit_answer, name='judge'),
    path('problem_bank/', views.ProblemBank.as_view(), name='problem_bank'),
    path('problem_bank/single_problem', views.SingleProblem.as_view(), name='problem_single'),
    path('teacher/test/manual-generation', views.ManualTestGeneration.as_view(), name='manual_test_generation'),
    path('teacher/test/auto-generation', views.AutoTestGeneration.as_view(), name='auto_test_generation'),
    path('statistics/teacher/tests', views.TeacherStatisticsTests.as_view(), name='teacher_statistics_tests'),
    path('statistics/teacher/chapters', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters'),
    path('statistics/teacher/knowledge_points', views.TeacherStatisticsKnowledgePoints.as_view(),
         name='teacher_statistics_knowledge_points'),
    path('statistics/student/', views.StudentStatistics.as_view(), name='student_statistics'),
    path('test_statistics/<int:pk>/', views.TestStatistics.as_view(), name='test_statistics'),
    path('test_statistics/<int:pk>/<int:student_pk>/', views.TestStatisticsStudentRecord.as_view(),
         name='test_statistics_student_record'),
    path('test_statistics/teacher/<int:pk>/<int:student_pk>/', views.TestStatisticsTeacherRecord.as_view(),
         name='test_statistics_teacher_record'),
    # path('chapter_statistics/<int:pk>', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters')
]
