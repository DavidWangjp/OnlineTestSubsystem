from django.urls import path

from . import views

app_name = 'online_test'
urlpatterns = [
    path('subjects', views.SubjectsView.as_view(), name='subjects'),
    path('subject/<int:subject>/tests', views.TestsView.as_view(), name='tests'),
    path('test/<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    path('test/submit_answer/', views.submit_answer, name='judge'),
    path('subject/<int:subject>/statistics/teacher/tests', views.TeacherStatisticsTests.as_view(),
         name='teacher_statistics_tests'),
    path('subject/<int:subject>/statistics/teacher/chapters', views.TeacherStatisticsChapters.as_view(),
         name='teacher_statistics_chapters'),
    path('subject/<int:subject>/statistics/teacher/knowledge_points', views.TeacherStatisticsKnowledgePoints.as_view(),
         name='teacher_statistics_knowledge_points'),
    path('subject/<int:subject>/statistics/student/', views.StudentStatistics.as_view(), name='student_statistics'),
    path('test_statistics/<int:pk>/', views.TestStatistics.as_view(), name='test_statistics'),
    path('test_statistics/<int:pk>/<int:student_pk>/',
         views.TestStatisticsStudentRecord.as_view(), name='test_statistics_student_record'),
    path('test_statistics/teacher/<int:pk>/<int:student_pk>/',
         views.TestStatisticsTeacherRecord.as_view(), name='test_statistics_teacher_record'),
    # path('chapter_statistics/<int:pk>', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters')
]
