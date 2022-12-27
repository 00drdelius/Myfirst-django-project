from multiprocessing import context
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout as auth_logout
from django.contrib import messages
from .forms import Login_Register_Form, User_Profile_Register_Form
from .models import User, Profiles
from full_test.models import VideoUpload
from django.core.cache import cache
import time

# Create your views here.

def userRegister(request):
    context={}
    if request.method == 'POST':
        register_form=Login_Register_Form(request.POST)
        if register_form.is_valid():
            new_user_model=register_form.save()
            new_ser_profile_initialised=Profiles.objects.create(connected=new_user_model)
            login(request, new_user_model)
            return redirect('full_test:index')
        else:
            messages.error(request, 'Sorry! The username or password is invalid!')
    else:
        register_form=Login_Register_Form()
    context['form']=register_form
    return render(request, 'users/register.html', context)



def userLogin(request):
    context={}
    context['form']=Login_Register_Form()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.filter(username=username).exists()
        except:
            messages.error(request, 'Sorry! User does not exist!')

        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('full_test:index')

    return render(request, 'users/login.html', context)


def userLogout(request):
    auth_logout(request)
    return redirect('full_test:index')



#based on class views trial
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin



decorators=[login_required, cache_page(60*5)] #another for caching server
@method_decorator(decorators, name='get')
class userHomepage(TemplateResponseMixin, SingleObjectMixin, View):
    template_name='users/user_homepage.html'
    
    #Rewrite get_objet method to prevent from the built-in query lookup!
    def get_object(self, queryset=None):
        return 

    def get_queryset(self):
        user_info=User.objects.get(username__exact=self.kwargs.get('username'))

        user_profile=Profiles.objects.get(connected_id=user_info.id)

        return user_info, user_profile

    def get_context_data(self, **kwargs):
        context={}
        context['user_info']=self.get_queryset()[0]
        context['user_profile']=self.get_queryset()[1]
        context.update(kwargs)
        return context


    def get(self, request, **kwargs):

        self.object=self.get_object()
        context=self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


'''
decorators=[login_required, ]
@method_decorator(decorators, name='get')
class history(View, SingleObjectMixin):
    template_name='users/user_history.html'
    clicked_video_lists = []

    #Must rewrite this method to prevent the built-in model query lookup
    def get_object(self, queryset=None):
        return 

    def get_queryset(self, request):
        if '/history' in request.path and 'X-Requested-With' in request.headers and request.method == 'GET':
            cilcked_video = VideoUpload.objects.get(videoTitle__exact=self.kwargs.get('clicked_videopage'))
            self.clicked_video_lists.append(cilcked_video)
            if len(self.clicked_video_lists) > 50:
               self.clicked_video_lists.pop(0)
        return self.clicked_video_lists


    def get_context_data(self,request, **kwargs):
        context={}
        context['history_video'] = self.get_queryset(request)
        cache.set('history_video', context['history_video'], 900)
        if kwargs:
            context.update(kwargs)
        return context


    def get(self, request, *args, **kwargs):
        if cache.get('history_video'):
            context = cache.get('history_video')
            return render(request, self.template_name, context)
        else:
            context = self.get_context_data(request, **kwargs)
            return render(request, self.template_name, context)
'''


@login_required
def userSettings(request, **kwargs):
    context={}
    username=kwargs.pop('username')
    user_update_profile=Profiles.objects.get(connected=request.user)
    if request.method == 'POST':
        user_profiles_form=User_Profile_Register_Form(instance=user_update_profile, data=request.POST, files=request.FILES)
        if user_profiles_form.is_valid():
            user_profile=user_profiles_form.save(commit=False)
            user_profile.connected_id=request.user.id
            user_profile.save(force_update=True)
            return redirect('users:Homepage', username=username)
    else:
        user_profile=User_Profile_Register_Form()    
    
    context['form']=user_profile
    return render(request, 'users/user_settings.html', context)


@login_required
def userVideos(request, **kwargs):
    context={}
    myvideos_list=VideoUpload.objects.filter(user=request.user)
    context['displayed_myvideos_list']=myvideos_list
    return render(request, 'users/user_myvideos.html', context)



'''
def formTest(request):
    context={}
    context['form']=User_Profile_Register_Form()
    return render(request, 'users/formtest.html', context)
'''





