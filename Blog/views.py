from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(ListView):
    model = News
    template_name = "Blog/home.html"
    context_object_name = "news" #This stores the name of the list


class DetailPage(DetailView):
    model = News
    template_name = "Blog/detail.html"
    context_object_name = "news"

class CreateNewsPage(CreateView):
    model = News
    fields = ["headline","content","image","reporter"]
    template_name = "Blog/create-views.html"
    success_url = "/"

class EditNewsPage(UpdateView):
    model = News
    fields = ["headline","content","image","reporter"]
    template_name = "Blog/update-news.html"
    success_url = "/"


class DeleteNewsPage(DeleteView):
    model = News
    template_name = "Blog/delete-news.html"
    success_url = "/"
    





#def home_page(request):
    #news = News.objects.all()
    #context = {
        #"news": news
   # }
    #return render(request, 'blog/home.html', context)


#def detail_page(request,id):
    #context = {
       # "news":news
    #}
    #return render(request, 'blog/detail.html', context)
