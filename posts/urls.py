from django.conf.urls import url
from .import views 
# I copied this 
urlpatterns = [
	url(r'^list/$',views.post_list, name ="list"),
	# url(r'^detail/$',views.post_detail, name ="detail"),
	#etha 7a6ena  id= #/(?P<post>[\w]+) ya3ni *** there will be a pramter number
	url(r'^detail/(?P<post_slug>[-\w]+)/$',views.post_detail, name ="detail"),
	url(r'^create/$', views.post_create, name ="create"),
	url(r'^update/(?P<post_slug>[-\w]+)/$',views.post_update, name ="update"),
	url(r'^delete/(?P<post_slug>[-\w]+)/$',views.post_delete, name ="delete"),
	url(r'^like_button/(?P<post_id>\d+)/$',views.like_button, name ="like_button"),
	url(r'^sign_up/$',views.usersignup, name ="sign_up"),
	url(r'^log_in/$',views.userlogin, name ="log_in"),
	url(r'^log_out/$',views.userlogout, name ="log_out"),


	# url(r'^delete/(?P<post_slug>[\w]+)/$', views.post_delete, name="delete"),

]




