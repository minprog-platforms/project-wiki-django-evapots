from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django import forms
import markdown
from . import util
import random


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title new entry")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'style': "width:100%;"}),
        label="Content new entry")

class EditPageForm(forms.Form):
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'style': "width:100%;"}),
        label="Content of Entry")

class SearchEntryForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "search",
        "placeholder": "Search Encyclopedia"}))


def entry_search(request):

    # if search form is submitted
    if request.method == "POST":
        form = SearchEntryForm(request.POST)

        # if form is valid, retrieve content of entry by title
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry_content = util.get_entry(title)

            # if entry already exists, redirect to entry 
            if entry_content:
                return redirect(reverse('entry', args=[title]))
            
            # else redirect to related titles search page 
            else:
                related_titles = util.related_titles(title)
                return render(request, "encyclopedia/search.html", {
                "related_titles": related_titles,
                "title": title,
                "search_form": SearchEntryForm()
                })

    # whenever form not valid, return to index page
    return redirect(reverse('index'))


def entry_new_page(request):

    # if new page button is clicked, redirect to create new page
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html", 
        {"search_form": SearchEntryForm(), "form": NewPageForm()})
    
         
    # if new page form is submitted
    if request.method == "POST":
        form = NewPageForm(request.POST)

        # if form is valid, retrieve title and content of new page
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            # if entry already present, return error message
            if title in util.list_entries():
                messages.error(request, "Please enter an entry title that is not yet present in the encyclopedia!")

            # otherwise, create and save new entry and redirect to this page
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', args=[title]))


def entry_edit(request, entry):

    # if edit page button is clicked, retrieve content redirect to edit page
    if request.method == "GET":
        content = util.get_entry(entry)
        return render(request, "encyclopedia/edit.html", 
        {"search_form": SearchEntryForm(), "form": EditPageForm(initial={'content':content}), "entry":entry})


    # if edit page form is submitted
    elif request.method == "POST":
        form = EditPageForm(request.POST)

        # if edit is valid, save adjustments and redirect to entry page
        if form.is_valid():
            text = form.cleaned_data['content']
            util.save_entry(entry, text)
            return redirect(reverse('entry', args=[entry]))
   

def index(request):

    # find all entries and redirect to index page
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries, "search_form": SearchEntryForm()
    })


def entry_view(request, entry):

    # retrieve list of entries
    entries = util.list_entries()

    # if entered entry in list, convert md to html 
    if entry in entries:
        with open('entries/' + entry + '.md', 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

            # redirect to entry page
            return render(request, "encyclopedia/entry.html", {
                "entry": entry, "content" : html, "search_form": SearchEntryForm()})
    
    # if entered entry is not in list, redirect to error page
    else:
        return render(request, "encyclopedia/error.html", {"search_form": SearchEntryForm()})


def entry_random(request):

    # retrieve random title from list of entries
    titles = util.list_entries()
    title = random.choice(titles)

    # redirect to selected entry page
    return redirect(reverse('entry', args=[title]))


