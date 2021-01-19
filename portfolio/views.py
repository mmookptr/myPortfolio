from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .form import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.save()
    else:
        form = ContactForm()
    return render(request, 'portfolio/index.html', {'form': form})
    
