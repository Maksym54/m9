from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, AuthorForm, QuoteForm
from .models import Author, Quote

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('quote_detail', pk=quote.pk)
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'quotes': quotes})