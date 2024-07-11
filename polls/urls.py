from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/thanks_for_voting/", views.ThanksView.as_view(), name="thanks_for_voting"),
    path("<int:pk>/results_info/", views.ResultsInfoView.as_view(), name="results_info"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]