from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from posts.models import Post

class PostListView(ListView):

    model = Post
    paginate_by = 100  # if pagination is desired


from django.views.generic.list import DetailView

from posts.models import Post
class PostDetailView(DetailView):
    model = Post


from django.views.generic.list import CreateView

from posts.models import Post
class PostCreateView(CreateView):
    
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

from django.views.generic.list import UpdateView


from posts.models import Post
class PostDeleteView(DeleteView):

    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


from django.views.generic.list import DeleteView

from posts.models import Post
class PostDeleteView(DeleteView):
    
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

