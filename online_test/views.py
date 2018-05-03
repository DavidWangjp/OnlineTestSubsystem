from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Test


class IndexView(generic.ListView):
    template_name = 'online_test/index.html'
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects


class TestDetail(generic.DetailView):
    model = Test
    template_name = 'online_test/test_detail.html'
