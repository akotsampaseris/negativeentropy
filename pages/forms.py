from django import forms

class ContactForm(forms.Form):
    sender  = forms.EmailField(
        label="E-mail:",
        required=True
    )
    
    subject = forms.CharField(
        label="Subject:",
        max_length=255,
        required=True
    )

    message = forms.CharField(
        label="Your message:",
        widget=forms.Textarea,
        required=False
   )
