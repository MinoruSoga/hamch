from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView, View, CreateView
from . import models
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q


# Create your views here.
class IndexView(TemplateView):
    # template_name = 'app/index.html'
    template_name = 'hamch/index.html'
    model = models.Post
    def get(self, request, *args, **kwargs):
        posts = self.model.objects.all().annotate(comment_count=Count("comments")).order_by("created_at")
        try_posts = self.model.objects.all().order_by('-try_count')[:5]
        try_done_posts = self.model.objects.all().order_by('-try_done_count')[:5]
        categories = models.Category.objects.all()
        return render(request, self.template_name, {'posts': posts, 'try_posts':try_posts, 'try_done_posts':try_done_posts, 'categories':categories})

class PostCreateView(TemplateView):
    template_name = "hamch/create.html"
    model = models.Post
    def get(self, request, *args, **kwargs):
        categories = models.Category.objects.all()
        try_posts = self.model.objects.all().order_by('-try_count')[:5]
        try_done_posts = self.model.objects.all().order_by('-try_done_count')[:5]
        return render(request, self.template_name, {'categories': categories, 'try_posts':try_posts, 'try_done_posts':try_done_posts})

    def post(self, request, *args, **kwargs):
        category_id = models.Category.objects.get(pk=request.POST['category'])
        if request.POST['name'] == None:
            name = '名無しさん'
        else:
            name = request.POST['name']

        self.model.objects.create(
            subject=request.POST['subject'],
            content=request.POST['content'],
            name=name,
            category=category_id,
            )
        return redirect('hamch:index')

class CategoryCreateView(TemplateView):
    template_name = "hamch/category-create.html"
    model = models.Category
    def get(self, request, *args, **kwargs):
        categories = models.Category.objects.all()
        try_posts = models.Post.objects.all().order_by('-try_count')[:5]
        try_done_posts = models.Post.objects.all().order_by('-try_done_count')[:5]
        return render(request, self.template_name, {'categories': categories, 'try_posts':try_posts, 'try_done_posts':try_done_posts})

    def post(self, request, *args, **kwargs):
        self.model.objects.create(
            name=request.POST['category'],
            )
        return redirect('hamch:create')

class PostDetailView(TemplateView):
    template_name = 'hamch/detail.html'
    model = models.Post
    def get(self, request, *args, **kwargs):
        post = self.model.objects.get(pk=kwargs['pk'])
        comments = models.Comment.objects.filter(post=kwargs['pk'])
        try_posts = self.model.objects.all().order_by('-try_count')[:5]
        try_done_posts = self.model.objects.all().order_by('-try_done_count')[:5]
        
        return render(request, self.template_name, {'post': post, 'comments': comments, 'try_posts':try_posts, 'try_done_posts':try_done_posts})

    def post(self, request, *args, **kwargs):
        post = self.model.objects.get(pk=kwargs['pk'])
        models.Comment.objects.create(
            content=request.POST['content'],
            name=request.POST['name'],
            post=post,
            )
        return redirect('hamch:detail', pk=kwargs['pk'])

class CountUpTryView(TemplateView):
    template_name = 'hamch/detail.html'
    model = models.Post
    def get(self, request, *args, **kwargs):
        post = self.model.objects.get(pk=kwargs['pk'])
        post.try_count += 1
        post.save()
        comments = models.Comment.objects.filter(post=kwargs['pk'])
        
        return render(request, self.template_name, {'post': post, 'comments': comments})
class CountUpTryDoneView(TemplateView):
    template_name = 'hamch/detail.html'
    model = models.Post
    def get(self, request, *args, **kwargs):
        post = self.model.objects.get(pk=kwargs['pk'])
        post.try_done_count += 1
        post.save()
        comments = models.Comment.objects.filter(post=kwargs['pk'])

        return render(request, self.template_name, {'post': post, 'comments': comments})
class SearchView(TemplateView):
    template_name = 'hamch/search.html'
    model = models.Post
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        if keyword:
            posts = self.model.objects.filter(
                 Q(name__icontains=keyword)|
                 Q(subject__icontains=keyword)|
                 Q(content__icontains=keyword)|
                 Q(category__name__icontains=keyword)
               ).annotate(comment_count=Count("comments")).order_by("created_at")
            # messages.success(request, '「{}」の検索結果'.format(keyword))
            message = '「{}」の検索結果'.format(keyword)
        try_posts = self.model.objects.all().order_by('-try_count')[:5]
        try_done_posts = self.model.objects.all().order_by('-try_done_count')[:5]
        return render(request, self.template_name, {'posts': posts, 'try_posts':try_posts, 'try_done_posts':try_done_posts, 'message': message})