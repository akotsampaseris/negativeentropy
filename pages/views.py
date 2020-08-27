from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import ContactForm

from blog.models import Post
from portfolio.models import Website

# Create your views here.
def home(request):
    posts = Post.objects.all()[:4]
    websites = Website.objects.all()[:4]

    context = {
        "posts": posts,
        "websites": websites
    }

    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender  = form.cleaned_data['sender']
            #name    = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            mail_to = ['a.kotsampaseris@technologic.gr']
            body = (
                'From: %s\n' \
                'Subject: %s\n\n' \
                'Message: %s'
            ) % (sender, subject, message)
            email = EmailMessage(
                subject,
                body,
                sender,
                mail_to,
                reply_to=[sender]
            )

            try:
                email.send()
                messages.success(request, 'Thanks for your message! I will try to reply soon!')
                return redirect('pages:contact')
            except:
                messages.error(request, 'Your message was not sent! Try again later!')
                return redirect('pages:contact')
    else:
        form = ContactForm()

    context = {
        "form": form
    }

    return render(request, 'pages/contact.html', context)
