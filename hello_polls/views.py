from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from hello_polls.models import MyChoice, MyPoll

def index(request):
    latest_poll_list = MyPoll.objects.all().order_by('-pub_date')[:3]
    return render_to_response('hello_polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/detail.html', {'MyPoll': p}, context_instance=RequestContext(request))
   
def results(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/results.html', {'MyPoll': p})

def vote(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    try:
        selected_choice = p.mychoice_set.get(pk=request.POST['MyChoice'])
    except (KeyError, MyChoice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('hello_polls/detail.html', {
            'MyPoll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hello_polls.views.results', args=(p.id,)))
        
# The below code is for generic views, which are not working as of the current version.        
#        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))