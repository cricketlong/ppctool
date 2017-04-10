from django.http import HttpResponse
from django.template import loader
from .models import Keyword

def index(request):
    if 'keyword' in request.POST:
        keyword = request.POST['keyword']
        results = Keyword.objects.filter(name=keyword).select_related()
    else:
        results = None

    keywords = Keyword.objects.select_related()
    template = loader.get_template('index.html')
    context = {
        'keywords': keywords,
        'results': results,
    }

    return HttpResponse(template.render(context, request))

def full_table(request):
    keywords = Keyword.objects.all()
    template = loader.get_template('index.html')
    context = {
        'keywords': keywords,
    }

    return HttpResponse(template.render(context, request))
