from django import forms
from .models import Test, ChoiceQuestionAnswerRecord, ChoiceQuestion, TrueOrFalseQuestionAnswerRecord, \
    TrueOrFalseQuestion, Student, Teacher, Chapter, KnowledgePoint, ProblemSearch

class ProblemSearchForm(forms.ModelForm):
	class Meta:
		model = ProblemSearch
		fields = ('problem_type', 'subject', 'chapter', 'knowledgePoint', 'creator')