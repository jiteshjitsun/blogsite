from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Category, Post
from .forms import  PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.forms.fields import DateTimeField
from django.http import HttpResponseRedirect


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-publish_time']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'(forms.py taking care of everything so no need to declare fields here)

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_post  = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-',' '), 'category_post':category_post})

# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('details', args = [str(pk)]))