from django.db import models
from django.db import models
# Create your models here.


#creat the blog model
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title


#set the admin page for BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')


#regist the model
admin.site.register([BlogPost,BlogPostAdmin])