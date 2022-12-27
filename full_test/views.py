from distutils.command.upload import upload
from email import contentmanager
from django.shortcuts import render, redirect
from . import forms
from django.http import JsonResponse
import time
from .models import VideoUpload, commentModel
from django.template import loader
from django.views import View
from django.views.generic.detail import SingleObjectMixin, SingleObjectTemplateResponseMixin
from users.models import User, Profiles
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

'''def searchByUrl(request, search_query):
    search_query=str(search_query)
    Video=VideoUpload.objects.filter(videoTitle__icontains=search_query)
    context['Video']=Video
    return render(request, 'full_test_templates/videoSearch.html', context)
'''

def searchByGet(request):
    context={'searching..':'searching..'}
    if request.method == 'GET':
        search_query=request.GET.get('search-box')
        Video=VideoUpload.objects.filter(videoTitle__icontains=search_query)
        context['searched_items']=Video
        return render(request, 'full_test_templates/videoSearch.html', context)

def ajax_result(request):
    context={}
    if 'X-Requested-With' in request.headers and request.method == 'GET':
        search_name=request.GET['search_name']
        context['count']=VideoUpload.objects.filter(videoTitle__icontains=search_name).count()
        #context['searched_displayed_list']=VideoUpload.objects.filter(videoTitle__icontains=search_name)
        return JsonResponse(context)

@cache_page(60*10, key_prefix='index_cache')
def index(request):
    context={'index':'index'}
    context['displayed_items']=VideoUpload.objects.all()
    #The quality of the user_profile should be qualified.
    if request.user.is_authenticated:
        '''
        user_brief={
            'username':User.objects.get(username=request.user.username),
            'user_profile':Profiles.objects.get(connected_id=request.user.id)
        }
        context.update(user_brief)
        '''
    return render(request, 'full_test_templates/index.html', context)

@login_required    #New
def videoUpload(request):
    context={'VideoUpload':'VideoUpload'}
    if request.method != 'POST':
        form = forms.videoUploadForm()
    else:
        form = forms.videoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.user = request.user
            form.save()
            time.sleep(3)
            return redirect ('full_test:index')
    context['form']=form
    return render(request, 'full_test_templates/videoUploading.html', context)



def VideoPage(request, id):
    context={'VideoPage':'VideoPage'}
    video_displayed=VideoUpload.objects.get(videoID=id)
    context['video_displayed']=video_displayed
    context['other_videos']=VideoUpload.objects.all()
    context['commentform']=forms.commentForm()
    return render(request, 'full_test_templates/VideoPage.html', context)

#from django.views.decorators.csrf import csrf_exempt



def ajax_comment(request, id):
        if 'X-Requested-With' in request.headers and request.method == 'POST':
            uploading_comment = forms.commentForm(request.POST)
            if uploading_comment.is_valid():
                uploaded_comment=uploading_comment.save(commit=False) #change form type to model type
                uploaded_comment.user = request.user
                uploaded_comment.video = VideoUpload.objects.get(videoID=id)
                uploaded_comment.save()
                return JsonResponse({'status':'success'})

def ajax_getComment(request, id):
    context={}
    if 'X-Requested-With' in request.headers and request.method == 'GET':
        comments = commentModel.objects.filter(video_id__exact=id)
        context['comments']=comments
        context['comment_user_profile']=Profiles.objects.filter(connected_id__in=[i.user_id for i in comments])
        return render(request, 'full_test_templates/commentPart.html', context)
