from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Like
from .forms import PostForm, UserSignUp, UserLogin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from urllib.parse import quote
from django.http import Http404, JsonResponse
from urllib.parse import quote
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate



def usersignup(request):
    context = {}
    form = UserSignUp()
    context ['form'] = form

    if request.method == "POST":
        form = UserSignUp (request.POST)
        if form.is_valid():
            user = form.save()
            x = user.username
            y = user.password

            user.set_password(y)
            user.save()

            auth = authenticate(username=x, password=y)
            login(request, auth)


            return redirect("list")
        messages.warning(request,form.errors)
        return redirect("list")
    return render(request,'sign_up.html', context)


def userlogin(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    if request.method == "POST":
        form = UserLogin(request.POST)
    if form.is_valid():
        some_username = form.cleaned_data['username']
        some_password = form.cleaned_data['password']
        auth = authenticate(username=some_username, password=some_password)
        if auth is not None:
            login(request, auth)
            return redirect("list")
            messages.warning(request, 'incorrect username/password combination')
            return redirect ("log_in")
            messages.warning(request, form.errors)
            return redirect("log_in")
    return render(request, 'log_in.html', context)

def userlogout(request):
    logout(request)
    return redirect("log_in")

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


    if request.user.is_authenticated():
        if Like.objects.filter(post=item, user=request.user).exists():
            liked = True 
        else:
            liked = False

    like_count = item.like_set.count()
    context = {
        "item" : item,
        "liked" : liked,
        "liked_count" : like_count,
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

def like_button(request, post_id):
    post_object = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(user=request.user, post=post_object)
    if created:
        action = "like"
    else:
        like.delete()
        action = "unlike"

    like_count = post_object.like_set.count()    
    response = {
    "like_count": like_count,
    "action": action,
    }
    return JsonResponse(response, safe=False)