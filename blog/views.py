from django.shortcuts import render

# Create your views here.


def list_view(request):
    return render(request, "blog/list/list.html")


def detail_view(request, slug):
    context = {"slug": slug}
    return render(request, "blog/detail/detail.html", context)
