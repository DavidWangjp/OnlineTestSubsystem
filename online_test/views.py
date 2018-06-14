from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.views import generic
import json
from .models import Test, ChoiceQuestionAnswerRecord, ChoiceQuestion, TrueOrFalseQuestionAnswerRecord, \
    TrueOrFalseQuestion


class IndexView(generic.ListView):
    model = Test
    template_name = 'online_test/index.html'


class TestDetail(generic.DetailView):
    model = Test
    template_name = 'online_test/test_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['choice_question_answer_record'] = {}
        for record in ChoiceQuestionAnswerRecord.objects.filter(test=self.object):
            context['choice_question_answer_record'][record.id] = record.answer

        context['true_or_false_question_answer_record'] = {}
        for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=self.object):
            context['true_or_false_question_answer_record'][record.id] = 'T' if record.answer else 'F'

        return context


class ProblemBank(generic.ListView):
    model = Test
    template_name = 'online_test/problem_bank.html'


def submit_answer(request: HttpRequest):
    if request.method == 'POST':
        test_id = int(request.POST['test_id'])
        question_type = request.POST['type']

        if question_type == 'choice':
            for key, value in request.POST.items():
                print(key, value)
                if key != 'test_id' and key != 'type':
                    try:
                        record = ChoiceQuestionAnswerRecord.objects.get(test=test_id)
                        record.answer = value
                        record.answer_time = timezone.now()
                        record.save()
                    except ChoiceQuestionAnswerRecord.DoesNotExist:
                        record = ChoiceQuestionAnswerRecord(
                            test=Test.objects.get(id=test_id),
                            question=ChoiceQuestion.objects.get(id=key),
                            student=None,
                            answer=value,
                            answer_time=timezone.now()
                        )
                        record.save()

        elif question_type == 'true_or_false':
            for key, value in request.POST.items():
                if key != 'test_id' and key != 'type':
                    print(key, value)
                    try:
                        record = TrueOrFalseQuestionAnswerRecord.objects.get(test=test_id)
                        record.answer = (value == 'T')
                        record.answer_time = timezone.now()
                        record.save()
                    except TrueOrFalseQuestionAnswerRecord.DoesNotExist:
                        record = TrueOrFalseQuestionAnswerRecord(
                            test=Test.objects.get(id=test_id),
                            question=TrueOrFalseQuestion.objects.get(id=key),
                            student=None,
                            answer=(value == 'T'),
                            answer_time=timezone.now()
                        )
                        record.save()

    return HttpResponse(json.dumps({'success': True, 'result': 'ok'}))
