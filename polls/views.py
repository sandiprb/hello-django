from django.shortcuts import render
from django.http import HttpResponse
from django.utils.functional import SimpleLazyObject

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.all().values()
	print (latest_question_list)
	template = 'polls/index.html'
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, template, context)


def detail(request, question_id):
	print(request)
	return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)