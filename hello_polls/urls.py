from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from hello_polls.models import MyPoll

urlpatterns = patterns('hello_polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
# The code for generic views is not working as of the current version.
#urlpatterns = patterns('',
#    url(r'^$',
#        ListView.as_view(
#            queryset=MyPoll.objects.order_by('-pub_date')[:3],
#            context_object_name='latest_poll_list',
#            template_name='hello_polls/index.html')),
#    url(r'^(?P<pk>\d+)/$',
#        DetailView.as_view(
#            model=MyPoll,
#            template_name='hello_polls/detail.html')),
#    url(r'^(?P<pk>\d+)/results/$',
#        DetailView.as_view(
#            model=MyPoll,
#            template_name='hello_polls/results.html'),
#        name='mypoll_results'),
#    url(r'^(?P<MyPoll_id>\d+)/vote/$', 'hello_polls.views.vote'),
#)