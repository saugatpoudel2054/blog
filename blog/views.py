from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from . import models
# Create your views here.
class DefaultView(ListView):
    model = models.Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'detail.html'

class AddNewArticle(CreateView):
    model = models.Article
    template_name = 'create.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = models.Article
    template_name = 'post_edit.html'
    fields = ['title', 'text']

class DeletePost(DeleteView):
    model = models.Article
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
