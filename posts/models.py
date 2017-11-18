from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User 
from django.utils import timezone 



class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, default=1)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=False)
    img = models.ImageField(null=True, blank=True, upload_to="post_images")
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish_date = models.DateField()
    draft = models.BooleanField(default=False)
    def __str__(self):
        return self.title

# to creat a model method ... funcction for an object it gives me the urls for detail using reverse it take details
    def get_detail_url(self):
        return reverse("detail", kwargs={"post_id":self.id})
    class Meta:
        ordering=['title']



def create_slug(instance, new_slug=None):
    slug_value = slugify(instance.title)
    if new_slug is not None:
        slug_value = new_slug

    query =Post.objects.filter(slug=slug_value)
    if query.exists():
        slug_value ="%s-%s"%(slug_value,query.last().id)
        return create_slug(instance, new_slug=slug_value)
    return slug_value

# when a post object before it save the object 
def pre_save_post_funtion(*args, **kwargs):
    instance = kwargs['instance']
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_funtion, sender=Post)
