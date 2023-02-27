from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title','summary','body','photo',)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','summary','body','photo','author',)

# Create your views here.
