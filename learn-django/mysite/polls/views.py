# @Author: @IamRezaMousavi
# @Date:   2023-02-10 16:51:21
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-10 22:28:45
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResualtView(generic.DetailView):
    model = Question
    template_name = 'polls/resualt.html'


def vote(request: HttpRequest, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice: Choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select any choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:resualt', args=(question_id,)))
