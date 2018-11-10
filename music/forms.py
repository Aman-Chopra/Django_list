from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'album_logo']
        labels = {
            'artist': ('Category'),
            'album_title': ('Details'),
            'album_logo':  ('Image')
        }

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
        labels = {
            'song_title': ('Item'),
            'audio_file': ('Audio remembrance')
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'email': ('Email'),
        }
