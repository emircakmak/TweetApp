from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=25, label="Nickname")
    message_input = forms.CharField(max_length=100, label="Message", widget=forms.Textarea(attrs={"class":"tweetmessage"}))
