from django.conf.urls import url

from . import views
from django.contrib import admin

app_name = 'online_test'
urlpatterns = [
    #   url('', views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url('test/(?P<pk>[0-9]+)/', views.TestDetail.as_view(), name='test_detail'),
    url('test/submit_answer/', views.submit_answer, name='judge'),
    url('teacher/test/manual-generation', views.ManualTestGeneration.as_view(), name='manual_test_generation'),
    url('statistics/teacher/tests', views.TeacherStatisticsTests.as_view(), name='teacher_statistics_tests'),
    url('statistics/teacher/chapters', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters'),
    url('statistics/teacher/knowledge_points', views.TeacherStatisticsKnowledgePoints.as_view(),
         name='teacher_statistics_knowledge_points'),
    url('statistics/student/', views.StudentStatistics.as_view(), name='student_statistics'),
    url('test_statistics/(?P<pk>[0-9]+)/', views.TestStatistics.as_view(), name='test_statistics'),
    url('test_statistics/(?P<pk>[0-9]+)/(?P<student_pk>[0-9]+)/', views.TestStatisticsStudentRecord.as_view(),
         name='test_statistics_student_record'),
    url('test_statistics/teacher/(?P<pk>[0-9]+)/(?P<student_pk>[0-9]+)/', views.TestStatisticsTeacherRecord.as_view(),
         name='test_statistics_teacher_record'),

    url('problem_bank/single_problem/choice/(?P<pk>[0-9]+)/', views.SingleChoice.as_view(), name='problem_choice'),
    url('problem_bank/single_problem/judge/(?P<pk>[0-9]+)/', views.SingleJudge.as_view(), name='problem_judge'),
    url('problem_bank/single_problem/static/choice/(?P<pk>[0-9]+)/', views.SingleStaticChoice.as_view(),
        name='static_choice'),
    url('problem_bank/single_problem/static/judge/(?P<pk>[0-9]+)/', views.SingleStaticJudge.as_view(),
        name='static_judge'),
    url('problem_bank/single_problem', views.SingleProblem.as_view(), name='problem_single'),
    url('problem_bank/search/', views.problem_search, name="problem_search"),
    url('problem_bank/add/', views.problem_add, name="problem_add"),
    url('problem_bank/(?P<pk>[0-9a-zA-Z]+)/mod/', views.problem_mod, name="problem_mod"),
    url('problem_bank/(?P<pk>[0-9]+)/del/', views.problem_del, name="problem_del"),
    url('problem_bank/detail/', views.ProblemDetail.as_view(), name="problem_detail"),
    url('problem_bank/', views.ProblemBank.as_view(), name='problem_bank'),

    url('teacher/test/auto-generation/(?P<pk>[0-9]+)/del/', views.test_del, name="test_del"),
    url('teacher/test/auto-generation/(?P<pk>[0-9]+)/mod/', views.test_mod, name="test_mod"),
    url('teacher/test/auto-generation/add/', views.test_add, name="test_add"),
    url('teacher/test/auto-generation/gerner/', views.test_gerner, name="test_gerner"),
    url('teacher/test/auto-generation/search/', views.test_search, name="test_search"),
    url('teacher/test/auto-generation', views.AutoTestGeneration.as_view(), name='auto_test_generation'),
    # url('chapter_statistics/(?P<pk>[0-9]+)', views.TeacherStatisticsChapters.as_view(), name='teacher_statistics_chapters')



    # path('subjects/student', views.SubjectsStudentView.as_view(), name='subjects_student'),
    # path('subjects/teacher', views.SubjectsTeacherView.as_view(), name='subjects_teacher'),
    # path('subject/<int:subject>/tests', views.TestsView.as_view(), name='tests'),
]
