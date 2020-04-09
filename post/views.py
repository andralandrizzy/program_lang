from django.shortcuts import render
from post.models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'post/index.html', context)