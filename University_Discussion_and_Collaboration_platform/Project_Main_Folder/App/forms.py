# forms.py
from django import forms

'''class UserEmailForm(forms.Form):
    email = forms.EmailField(label='Your Email', required=True)'''

from django import forms
from .models import Message

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['message'].widget.attrs.update({'placeholder': 'Type your reply here...'})

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['message'].widget.attrs.update({'placeholder': 'Type your reply here...'})