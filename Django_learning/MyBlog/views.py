from django.shortcuts import render

# Create your views here.


def myBlogs(request):
    blog_list = BlogPost.objects.all()
    return render_to_response("BlogTemplate.html",{'blog_list':blog_list})