from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, AddPostForm, EditPostForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
   model = Post
   template_name = 'home.html'
   ordering = ['-post_date']

class ArticleView(DetailView):
   model = Post
   template_name = 'article_details.html'

class AddBlogView(CreateView):
   model = Post
   form_class = AddPostForm
   template_name = 'addblog.html'
   # fields = '__all__'
   # fields = ('title', 'title_tag', 'body')
   def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateBlogView(UpdateView):
   model = Post
   form_class = EditPostForm
   template_name = 'updateblog.html'
   # fields = ['title', 'title_tag', 'body']
   
class DeleteBlogView(DeleteView):
   model = Post
   template_name = 'deleteblog.html'
   success_url = reverse_lazy('home')

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        blogs = Post.objects.filter(author=user)
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'dashboard.html',{'blogs':blogs,'full_name':full_name,'groups':gps})