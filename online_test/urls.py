from django.conf.urls import url

from . import views

app_name = 'online_test'
urlpatterns = [
    #url('', views.IndexView.as_view(), name='index'),
    url('test/<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    url('test/submit_answer/', views.submit_answer, name='judge'),
    url('problem_bank/single_problem', views.SingleProblem.as_view(), name='problem_single'),
    url('problem_bank/', views.ProblemBank.as_view(), name='problem_bank'),
    url('teacher/test/manual-generation', views.ManualTestGeneration.as_view(), name='manual_test_generation'),
    url('teacher/test/auto-generation', views.AutoTestGeneration.as_view(), name='auto_test_generation'),
    url('statistics/teacher/tests', views.TeacherStatisticsTests.as_view(), name='teacher_statistics_tests'),
    url('statistics/teacher/chapters', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters'),
    url('statistics/teacher/knowledge_points', views.TeacherStatisticsKnowledgePoints.as_view(),
         name='teacher_statistics_knowledge_points'),
    url('statistics/student/', views.StudentStatistics.as_view(), name='student_statistics'),
    url('test_statistics/<int:pk>/', views.TestStatistics.as_view(), name='test_statistics'),
    url('test_statistics/<int:pk>/<int:student_pk>/', views.TestStatisticsStudentRecord.as_view(),
         name='test_statistics_student_record'),
    url('test_statistics/teacher/<int:pk>/<int:student_pk>/', views.TestStatisticsTeacherRecord.as_view(),
         name='test_statistics_teacher_record'),

    url('problem_bank/search/', views.problem_search, name="problem_search"),
    url('problem_bank/add/', views.problem_add, name="problem_add"),
    url('problem_bank/mod/', views.problem_mod, name="problem_mod"),
    url('problem_bank/del/', views.problem_del, name="problem_del"),
    # url('chapter_statistics/<int:pk>', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters')
]
