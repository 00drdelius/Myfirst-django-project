from cProfile import label
from django import forms
from .models import VideoUpload, commentModel



class videoUploadForm(forms.ModelForm):
    class Meta:
        model=VideoUpload
        exclude=['user']
        #fields=['videoTitle','video','videoIntroduction']
        #fields='__all__'
        widgets={
            'videoTitle':forms.TextInput(attrs={'class': 'UploadVideoTitle'}),
            'video':forms.FileInput(attrs={'class':'UploadVideo'}),
            'videoIntroduction':forms.Textarea(
                attrs={'class':'UploadVideoIntron',
                'cols':'10',
                'rows':'5'}),
            'videoPoster':forms.FileInput(attrs={'class':'UploadvideoPoster'}),
        }
        labels={
            'videoPoster': 'Video poster',
        }


class commentForm(forms.ModelForm):
    class Meta:
        model=commentModel
        exclude=['user', 'user_comment_time', 'video']
        widgets={
            'user_comment':forms.TextInput(attrs={'class':'your-comment-place'}),  #the dict of request.POST should be the same or including 'user_comment'
        }