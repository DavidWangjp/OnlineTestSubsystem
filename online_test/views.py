import datetime

from django.http import HttpRequest, HttpResponse
from django.views import generic

from .models import Test, ChoiceQuestionAnswerRecord


class IndexView(generic.ListView):
    template_name = 'online_test/index.html'
    context_object_name = 'tests'

    def get_queryset(self):
        return Test.objects


class TestDetail(generic.DetailView):
    model = Test
    template_name = 'online_test/test_detail.html'


def judge(request: HttpRequest):
    if request.method == 'POST':
        test_id = request.POST['test_id']
        type = request.POST['type']
        if type == 'choice':
            for key, value in request.POST.items():
                if key != 'test_id' and key != 'type' and key != 'csrfmiddlewaretoken':
                    record = ChoiceQuestionAnswerRecord.objects.get(test=test_id)
                    if not record:
                        record = ChoiceQuestionAnswerRecord(test=test_id, question=int(key), student=None, answer=value,
                                                            answer_time=datetime.datetime.now())
                        record.save()
                    else:
                        record.answer = value
                        record.save()
    return HttpResponse('ok')
