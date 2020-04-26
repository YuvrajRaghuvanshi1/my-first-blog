from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.db.models import Q
    
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    item = Post.objects.get(pk=pk)
    if request.user == item.author:
      if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            return HttpResponse("INVALID FORM!")    
      else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})
    else:
        return HttpResponse("YOU CANNOT EDIT A POST YOU HAVE NOT WRITTEN!")


'''class post_edit(LoginRequiredMixin,UpdateView):
        #login_url = 'accounts/login/'
        redirect_field_name = 'blog/post_detail.html'
        #template_name='blog/post_edit.html'
        form_class = PostForm
        model = Post
        '''

def About(request):
   return  render(request,'blog/about.html')    

def search(request)    :
      if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'blog/base.html', context)

        else:
            return render(request, 'blog/post_list.html')

      else:
        return render(request, 'blog/post_list.html')   
