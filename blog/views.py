from django.shortcuts import render
from blog.models import Blog
# Create your views here.


def list_view(request):
    context = {'blogs': Blog.objects.all().order_by("-created")[:5]}
    return render(request, "blog/list/list.html", context)


def detail_view(request, slug):
    context = {}

    try:
        context['blog'] = Blog.objects.filter(slug=slug).first()
    except Exception as e:
        print(e)

    return render(request, "blog/detail/detail.html", context)
