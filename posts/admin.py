from django.contrib import admin
from .models import Post


class Post_info(admin.ModelAdmin):
	list_display =["title",'timestamp']
	search_fields =[ "title","content"]
	class Meta:
		model = Post
		

admin.site.register(Post, Post_info)