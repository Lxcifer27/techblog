from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, AddPostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
   model = Post
   template_name = 'home.html'
   # ordering = ['-post_date']

   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(HomeView, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu

      return context

class ArticleView(DetailView):
   model = Post
   template_name = 'article_details.html'

   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(ArticleView, self).get_context_data(*args, **kwargs)

      blogID = get_object_or_404(Post, id=self.kwargs['pk'])
      total_likes =blogID.total_likes()
      context["cat_menu"] = cat_menu
      context["total_likes"] = total_likes

      return context

class AddBlogView(CreateView):
   model = Post
   form_class = AddPostForm
   template_name = 'addblog.html'
   # fields = '__all__'
   # fields = ('title', 'title_tag', 'body')
   def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCategoryView(CreateView):
   model = Category
   # form_class = AddPostForm
   template_name = 'addcategory.html'
   fields = '__all__'
   # fields = ('title', 'title_tag', 'body')

   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context

def CategoryListView(request):
   cat_list = Category.objects.all()
   return render(request, 'category_list.html', {'cat_list': cat_list})

def CategoryView(request, cats):
   cats = cats.title().replace('-', ' ')
   # print(f"Filtering posts for category: {cats}")
   category_post = Post.objects.filter(category=cats)
   # print(f"Number of posts found: {category_post.count()}")
   return render(request, 'categories.html', {'cats': cats, 'category_post': category_post})


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

def LikeView(request, pk):
   post = get_object_or_404(Post, id=request.POST.get('post_id'))
   post.likes.add(request.user)
   return HttpResponseRedirect(reverse('article', args=[str(pk)]))