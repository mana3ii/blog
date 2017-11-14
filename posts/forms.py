from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
# class Meta is to make conection 		
		model = Post
		fields = ['title' , 'content', 'img']
		# min el model 