from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
# class Meta is to make conection 		
		model = Post
		fields = ['title' , 'content', 'img', 'author','publish_date']

		widgets ={
		'publish_date':forms.DateInput(attrs={"type":"date"}),
		}
		# min el model 