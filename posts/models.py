from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    img = models.ImageField(null=True, blank=True, upload_to="post_images")
    slug = models.SlugField()

    def __str__(self):
        return self.title


# to creat a model method ... funcction for an object it gives me the urls for detail using reverse it take details
    def get_detail_url(self):
        return reverse("detail", kwargs={"post_id":self.id})
    class Meta:
        ordering=['title']