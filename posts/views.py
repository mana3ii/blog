from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def post_home(request):
	return HttpResponse ("<h1> let's see </h1>")


def post_list(request):
	objects = Post.objects.all()
	context = {
	"post_items": objects,

	}
	return render(request,"list.html", context)


def post_detail(request, post):
	item = Post.objects.get(id=post)
	#item = get_object_or_404 (Post,id=post)
	context = {
	"item" : item,
	}
	return render (request, "detail.html", context)
