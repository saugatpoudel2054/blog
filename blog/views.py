from django.views.generic import ListView, DetailView
from . import models
# Create your views here.
class DefaultView(ListView):
    model = models.Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'detail.html'