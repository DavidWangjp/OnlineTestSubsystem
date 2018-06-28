from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.views import generic
import json
from .models import Test, ChoiceQuestionAnswerRecord, ChoiceQuestion, TrueOrFalseQuestionAnswerRecord, \
    TrueOrFalseQuestion, Student, Teacher, Chapter, KnowledgePoint, Subject

login_student = Student.objects.all()[0]
login_teacher = Teacher.objects.all()[0]


class SubjectsView(generic.ListView):
    model = Subject
    template_name = 'online_test/subjects.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = login_student.subjects.all()
        context['object_list'] = object_list
        return context


class TestsView(generic.ListView):
    model = Test
    template_name = 'online_test/tests.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        subject = Subject.objects.get(id=self.kwargs['subject'])

        context = super().get_context_data(**kwargs)
        object_list = Test.objects.filter(attend_students=login_student, subject=subject)
        context['object_list'] = object_list
        context['subject_id'] = subject.id
        return context


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


class TeacherStatisticsTests(generic.ListView):
    model = Test
    template_name = 'online_test/teacher_statistics_tests.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        subject = Subject.objects.get(id=self.kwargs['subject'])

        context = super().get_context_data(**kwargs)
        object_list = Test.objects.filter(creator=login_teacher, subject=subject)
        context['object_list'] = object_list
        context['subject_id'] = subject.id

        return context


class TeacherStatisticsChapters(generic.ListView):
    model = Chapter
    template_name = 'online_test/teacher_statistics_chapters.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        subject = Subject.objects.get(id=self.kwargs['subject'])

        object_list = {}
        for test in Test.objects.filter(creator=login_teacher, subject=subject):
            for record in ChoiceQuestionAnswerRecord.objects.filter(test=test):
                if record.question.chapter not in object_list.keys():
                    object_list[record.question.chapter] = {'correct_num': 0, 'total_num': 1}
                    if record.answer == record.question.solution:
                        object_list[record.question.chapter]['correct_num'] += 1
                else:
                    object_list[record.question.chapter]['total_num'] += 1
                    if record.answer == record.question.solution:
                        object_list[record.question.chapter]['correct_num'] += 1

            for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=test):
                if record.question.chapter not in object_list.keys():
                    object_list[record.question.chapter] = {'correct_num': 0, 'total_num': 1}
                    if record.answer == record.question.solution:
                        object_list[record.question.chapter]['correct_num'] += 1
                else:
                    object_list[record.question.chapter]['total_num'] += 1
                    if record.answer == record.question.solution:
                        object_list[record.question.chapter]['correct_num'] += 1
        context['object_list'] = object_list
        context['subject_id'] = subject.id

        return context


class TeacherStatisticsKnowledgePoints(generic.ListView):
    model = KnowledgePoint
    template_name = 'online_test/teacher_statistics_knowledge_points.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.get(id=self.kwargs['subject'])

        object_list = {}
        for test in Test.objects.filter(creator=login_teacher, subject=subject):
            print(test)
            for record in ChoiceQuestionAnswerRecord.objects.filter(test=test):
                if record.question.knowledge_point not in object_list.keys():
                    object_list[record.question.knowledge_point] = {'correct_num': 0, 'total_num': 1}
                    if record.answer == record.question.solution:
                        object_list[record.question.knowledge_point]['correct_num'] += 1
                else:
                    object_list[record.question.knowledge_point]['total_num'] += 1
                    if record.answer == record.question.solution:
                        object_list[record.question.knowledge_point]['correct_num'] += 1

            for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=test):
                if record.question.knowledge_point not in object_list.keys():
                    object_list[record.question.knowledge_point] = {'correct_num': 0, 'total_num': 1}
                    if record.answer == record.question.solution:
                        object_list[record.question.knowledge_point]['correct_num'] += 1
                else:
                    object_list[record.question.knowledge_point]['total_num'] += 1
                    if record.answer == record.question.solution:
                        object_list[record.question.knowledge_point]['correct_num'] += 1
        context['object_list'] = object_list
        context['subject_id'] = subject.id

        return context


class TestStatistics(generic.DetailView):
    model = Test
    template_name = 'online_test/test_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_score = 0

        assert isinstance(self.object, Test)

        for question in self.object.choice_questions.all():
            test_score += question.score

        for question in self.object.true_or_false_questions.all():
            test_score += question.score

        avg_score = 0
        student_scores = []
        for student in self.object.attend_students.all():
            student_info = {'id': student.id, 'name': student.name, 'score': 0}
            for record in ChoiceQuestionAnswerRecord.objects.filter(test=self.object, student=student):
                if record.answer == record.question.solution:
                    avg_score += record.question.score
                    student_info['score'] = student_info['score'] + record.question.score
            for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=self.object, student=student):
                if record.answer == record.question.solution:
                    avg_score += record.question.score
                    student_info['score'] = student_info['score'] + record.question.score
            student_scores.append(student_info)

        avg_score /= len(self.object.attend_students.all())

        context['avg'] = avg_score
        context['total'] = test_score

        context['students'] = student_scores
        return context


class TestStatisticsStudentRecord(generic.DetailView):
    model = Test
    template_name = 'online_test/test_statistics_student_record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = Student.objects.get(id=self.kwargs['student_pk'])

        T_score = 0
        T_total_score = 0
        C_score = 0
        C_total_score = 0
        choice_question_records = []
        for record in ChoiceQuestionAnswerRecord.objects.filter(test=self.object, student=student):
            choice_question_records.append(record)
            C_total_score += record.question.score
            if record.answer == record.question.solution:
                C_score += record.question.score

        true_or_false_question_records = []
        for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=self.object, student=student):
            true_or_false_question_records.append(record)
            T_total_score += record.question.score
            if record.answer == record.question.solution:
                T_score += record.question.score
        context['test'] = self.object
        context['choice_question_answer_record'] = choice_question_records
        context['true_or_false_question_answer_record'] = true_or_false_question_records
        context['T_score'] = T_score
        context['T_total_score'] = T_total_score
        context['C_score'] = C_score
        context['C_total_score'] = C_total_score
        return context


class TestStatisticsTeacherRecord(generic.DetailView):
    model = Test
    template_name = 'online_test/test_statistics_teacher_record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = Student.objects.get(id=self.kwargs['student_pk'])

        T_score = 0
        T_total_score = 0
        C_score = 0
        C_total_score = 0
        choice_question_records = []
        for record in ChoiceQuestionAnswerRecord.objects.filter(test=self.object, student=student):
            choice_question_records.append(record)
            C_total_score += record.question.score
            if record.answer == record.question.solution:
                C_score += record.question.score

        true_or_false_question_records = []
        for record in TrueOrFalseQuestionAnswerRecord.objects.filter(test=self.object, student=student):
            true_or_false_question_records.append(record)
            T_total_score += record.question.score
            if record.answer == record.question.solution:
                T_score += record.question.score
        context['test'] = self.object
        context['choice_question_answer_record'] = choice_question_records
        context['true_or_false_question_answer_record'] = true_or_false_question_records
        context['T_score'] = T_score
        context['T_total_score'] = T_total_score
        context['C_score'] = C_score
        context['C_total_score'] = C_total_score
        return context


class StudentStatistics(generic.ListView):
    model = Test
    template_name = 'online_test/student_statistics.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.get(id=self.kwargs['subject'])

        object_list = Test.objects.filter(attend_students=login_student, subject=subject)
        context['object_list'] = object_list
        context['student_id'] = login_student.id
        context['subject_id'] = subject.id

        return context


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
