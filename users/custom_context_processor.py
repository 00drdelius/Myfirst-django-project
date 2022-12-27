from sqlite3 import connect
from django.conf import settings
from .models import Profiles
from django.contrib.auth.models import User




def custom_template_contextrender_processor(request):
    '''
    Used to create a set of global contexts for template to render.
    Should be added in settings.TEMPLATES.OPTIONS.context_processors and restart the server.
    '''
    context={}  #Make the function surly get something to prevent return 'Nonetype' if user is not authenticated.

    if request.user.is_authenticated:
        user_brief={
            'username':User.objects.get(username=request.user.username),
            'user_profile':Profiles.objects.get(connected_id=request.user.id)
        }
        context.update(user_brief)
    return context