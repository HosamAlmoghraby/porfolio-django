from django.shortcuts import render
from base.models import SiteSetting
from pages.models import Page
from blog.models import Post


def index(request):
    settings        = SiteSetting.objects.get(pk=1)
    pages           = Page.objects.order_by('order').filter(active=True)
    object_list     = Post.objects.all()

    context = {
        'settings': settings,
        'pages': pages,
        'object_list': object_list
    }
    return render(request, 'pages/index.html', context)
