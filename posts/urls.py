from django.conf.urls import url
from . import views 
# I copied this 
urlpatterns = [
url(r'^list/$',views.post_list, name ="list"),
# url(r'^detail/$',views.post_detail, name ="detail"),
#etha 7a6ena  id= #/(?P<post>\d+) ya3ni *** there will be a pramter number
url(r'^detail/(?P<post>\d+)$',views.post_detail, name ="detail"),

]