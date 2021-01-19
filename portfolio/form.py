from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'contact-email',
                'id': 'email-field',
                'placeholder': 'Email'
            }),
        max_length=50,
        label = "" )
    topic = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'message-topic',
                'id': 'topic-field',
                'placeholder': 'Topic'
            }),
        max_length=50,
        label = "" )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'class': 'message',
                'id': 'message-field',
                'placeholder': 'Message',
                'rows': 4, 'cols':61
            }),

        label = "")

    class Meta:
        model = ContactMessage
        fields = ("email", "topic", "message")
