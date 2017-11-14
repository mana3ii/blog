from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


# Create your views here.
def post_home(request):
	return HttpResponse ("<h1> let's see </h1>")


def post_list(request):
	objects = Post.objects.all()
	paginator = Paginator(objects, 3) # Show 25 contacts per page

	number = request.GET.get('page')
	try:
		objects = paginator.page(number)

	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)


	context = {
	"post_items": objects,
	}
	return render(request,"list.html", context)


def post_detail(request, post_id):
	item = Post.objects.get(id=post_id)
	#item = get_object_or_404 (Post,id=post)
	context = {
	"item" : item,
	}
	return render (request, "detail.html", context)


def post_create (request):
	form =PostForm(request.POST or None)
	if form .is_valid():
		form.save()
		messages.success (request, 'your post was added')
		return redirect("list")
	context = {
		"form": form
	}
	return render(request, 'post_create.html' , context)
	
def post_update (request, post):
	item = Post.objects.get(id=post_id)
	form =PostForm(request.POST or None,request.FILES or None, instance=item)
	if form .is_valid():
		form.save()
		messages.info(request,"you changed the post")
		return redirect("list", post_id=item.id)
	context = {
		"form": form,
		"item": item,
	}
	return render(request, 'post_update.html' , context)


def post_delete(request,post_id):
	instance = get_object_or_404(Post, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("Posts=list")
