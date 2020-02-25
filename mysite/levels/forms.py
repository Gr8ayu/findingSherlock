from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User, Submissions

class submissionForm(forms.Form):
    # class Meta:
        # model = Submissions
        # fields = ('userID', 'level', 'key', 'date_time')
        # fields = ('userID', 'key' )
    
    username = forms.CharField(label='USERNAME ', max_length=50)
    key = forms.CharField(label='KEY ', max_length=50)
    level = forms.IntegerField(label='LEVEL', max_value=15, min_value = 1)
