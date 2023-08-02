from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# First view

def index(request):
    '''
    Index class and page displays the latest few questions
    '''
    return HttpResponse("First view")

def detail(request, question_id):
    '''
    Detail class and page displays the question text witout results but with a form to vote
    '''
    return HttpResponse("This is question %s. " % question_id)

def results(request, question_id):
    '''
    Results class or page displays results of a particular question
    '''
    return HttpResponse("You are looking at results of question %s. " % question_id)

def vote(request, question_id):
    '''
    The vote action classs or page handles voting for a particular choice in a particular question
    '''
    return HttpResponse("You are voting on question %s. " % question_id)
