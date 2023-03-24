from django.views.generic.list import ListView

from userprofile.models import Profile
from feeds.models import Feed


class FeedsListView(ListView):

    model = Feed
    paginate_by = 100
    
    template_name = 'home/index.html'
    context_object_name = 'feeds'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=1)
        
        return context