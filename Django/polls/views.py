from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()  # Fix the typo here: seleceted_choice → selected_choice
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
# @login_required
# def my_protected_view(request):
#     pass
# from django.contrib.auth.decorators import login_required

class QuestionListView(generic.ListView):
    model = Question  # Specify the model
    template_name = 'polls/question_list.html'  # Specify the template
    context_object_name = 'questions'  # Name of the list in the template context

# class ProtectedView(LoginRequiredMixin, TemplateView):
#     template_name = 'polls/protected_page.html'
#     # login_url = '/accounts/login/' # Optional: override default login URL
#     # redirect_field_name = 'redirect_to' # Optional: override query param name
