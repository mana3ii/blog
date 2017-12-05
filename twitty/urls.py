from django.conf.urls import url
from .import views 


urlpatterns = [
	url(r'^twitty/$',views.tweet_search, name ="twitty"),

]