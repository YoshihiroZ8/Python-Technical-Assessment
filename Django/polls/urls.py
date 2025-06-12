from django.urls import path
from . import views
from .views import QuestionListView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]