from django import forms
from .models import Match
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'match_time', 'venue', 'watch']
        widgets = {
            'match_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # HTML5 datetime input
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']