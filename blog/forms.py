from django.db import models as forms
from ckeditor.fields import RichTextFormField




class ContactForm(forms.Model):
    name = forms.CharField(max_length=200, help_text='Your name')
    email  = forms.EmailField(help_text="Your e-mail address")
    subject = forms.CharField(max_length=200)
    message = forms.TextField(null=True)
    updated_on = forms.DateTimeField(auto_now=True)
    created_on = forms.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.name

