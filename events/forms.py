# events/forms.py
from django import forms
from .models import Event, RSVP

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'category']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
'''class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['status']
        '''        
