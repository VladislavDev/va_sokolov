from django.shortcuts import render
from userprofile.models import Profile


def index(request):    

    context = {
        'profile': Profile.objects.get(pk=1),
    }

    return render(request, 'home/index.html', context)