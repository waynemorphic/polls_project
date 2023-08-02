from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote")
]

# Using angle brackets '<>', captures part of the URL and sends it to the kwarg** of the 
# view function. question_id part defines the name that is used to identify the matched pattern
# while the int part converts the pattern that should match this part of the url

# Therefore, the url is for instance /polls/2/vote -> You are voting on question 2