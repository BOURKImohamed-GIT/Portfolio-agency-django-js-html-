from django import forms
from django.db.models.fields import AutoField

from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ["Name", "country", "subject", "message", "Your_email", "mobile"]
        widgets = {'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name','required': True}),
                   'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your country','required': True}),
                   'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject','required': True}),
                   'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message','required': True}),
                   'Your_email': forms.EmailInput(attrs={'type':"email", 'class': 'form-control', 'placeholder': 'Your email/gmail','required': True}),
                   'mobile': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'Your mobile/whatsApp(optional)'}),
                   }
        readonly_fields = ["created_at"]
        
class CommentForm(forms.ModelForm):
    class  Meta:
        model=Comment
        fields = ["First_name", "Last_name","Email", "Comment"]
        widgets = {'First_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First_name','required': True}),
                           'Last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_name','required': True}),
                           'Email': forms.EmailInput(attrs={'type':"email", 'class': 'form-control', 'placeholder': 'Email','required': True}),

                           'Comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message','required': True}),
                          
                           }
        readonly_fields = ["created_at"]
        

class ReviewsForm(forms.ModelForm):
    class  Meta:
        model=Reviews
        fields = ["name","email", "text"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name','required': True}),
                         
                   'email': forms.EmailInput(attrs={'type':"email", 'class': 'form-control', 'placeholder': 'Email','required': True}),

                  'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message','required': True}),
                          
                           }
        readonly_fields = ["date"]



