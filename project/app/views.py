from django.shortcuts import render,redirect
from .forms import CreatePostsForm
from django.http import HttpResponse
import time


a= []
def index(request):
    CreateForm = CreatePostsForm()
    if request.method == "POST":
        CreateForm = CreatePostsForm(request.POST)
        if CreateForm.is_valid():
            name = CreateForm.cleaned_data["name"]
            url = CreateForm.cleaned_data["url"]
            content = CreateForm.cleaned_data["content"]
            published = CreateForm.cleaned_data["published"]
            category = CreateForm.cleaned_data["category"]
            if published == True:
                published = "Опубликовано"
                a.append([name, url, content, published, category])
                return redirect('news')
    return render(request,"index.html",{"form":CreateForm})

def news(request):
    return render(request,"news.html",{"news":a})