from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from urllib.parse import quote
from django.http import Http404
from urllib.parse import quote
from django.utils import timezone
from django.db.models import Q






# Create your views here.
def post_home(request):
    return HttpResponse ("<h1> let's see </h1>")


def post_list(request):
    today = timezone.now().date()
    object_list = Post.objects.filter(draft=False).filter(publish_date__lte=today)
    if request.user.is_staff or request.user.is_superuser:
        object_list = Post.objects.all()


    query = request.GET.get("hessa")
    if query:
        object_list = object_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)
            ).distinct()
    
    paginator = Paginator(object_list, 3) # Show 25 contacts per page

    number = request.GET.get('page')
    try:
        object_list = paginator.page(number)

    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)


    context = {
    "post_items": object_list,
    "title": "List",
    "user" :request.user,
    "today":today
    }
    return render(request,"list.html", context)


def post_detail(request, post_slug):
    item = Post.objects.get(slug=post_slug)
    #item = get_object_or_404 (Post,slug=post)
    context = {
    "item" : item,
    "share_string": quote(item.content)
    }
    return render (request, "detail.html", context)


def post_create (request):
    if not request.user.is_staff:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form .is_valid():
        create_post = form.save(commit=False)
        create_post.auther = request.user
        create_post.save()
        messages.success (request, 'your post was added')
        return redirect("list")
    context = {
        "form": form
    }
    return render(request, 'post_create.html' , context)

def post_update (request, post_slug):
    if not request.user.is_staff:
        raise http404

    item = Post.objects.get(slug=post_slug)
    form =PostForm(request.POST or None,request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.info(request,"you changed the post")
        return redirect("list")
    context = {
        "form": form,
        "item": item,
    }
    return render(request, 'post_update.html' , context)


def post_delete(request,post_slug):
    if not request.user.is_staff:
        raise Http404

    instance = get_object_or_404(Post, slug=post_slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("list")
