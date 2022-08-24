from django.http import Http404
from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        print("*"*33)
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Başarılı bir şekilde oluşturuldu.', extra_tags='mesaj basarili')
            return HttpResponseRedirect(post.get_absolute_url())

    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde kaydedildi.', extra_tags='mesaj basarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    import json
    post = get_object_or_404(Post, slug=slug)
    # post = Post.objects.get(slug)
    if request.user == post.user:
        Post.objects.filter(slug=slug).delete()
        post.delete()
        messages.success(request, 'Başarılı bir şekilde silindi.', extra_tags='mesaj basarili')
    return HttpResponse(json.dumps({'response': 'Başarılı !'}))


def my_posts(request):
    queryset = Post.objects.filter(user=request.user).order_by('publishing_date')
    paginator = Paginator(object_list=queryset, per_page=5)
    user_posts = paginator.page(request.GET.get('page', 1) or 1)
    return render(request=request, template_name="post/index.html", context={'posts': user_posts})

