from django.http import HttpResponse
from django.template import loader
from .models import Campaign, AdGroup, Keyword

def index(request):
    #campaigns = Campaign.objects.all()
    template = loader.get_template('index.html')
    context = {
        #'campaigns': campaigns,
    }

    return HttpResponse(template.render(context, request))

def compare(request):
    campaigns = Campaign.objects.all()
    template = loader.get_template('compare.html')
    context = {
        'campaigns': campaigns,
    }

    return HttpResponse(template.render(context, request))

def campaign(request, cid):
    campaign = Campaign.objects.get(id=cid)
    adgroups = AdGroup.objects.filter(campaign_id=cid)
    template = loader.get_template('campaign.html')
    context = {
        'adgroups': adgroups,
        'campaign': campaign,
    }

    return HttpResponse(template.render(context, request))

def adgroup(request, cid, agid):
    campaign = Campaign.objects.get(id=cid)
    adgroup = AdGroup.objects.get(id=agid)
    keywords = Keyword.objects.filter(adgroup_id=agid)
    template = loader.get_template('adgroup.html')
    context = {
        'campaign': campaign,
        'adgroup': adgroup,
        'keywords': keywords,
    }

    return HttpResponse(template.render(context, request))

def keyword(request, cid, agid, kid):
    campaign = Campaign.objects.get(id=cid)
    adgroup = AdGroup.objects.get(id=agid)
    keyword = Keyword.objects.get(id=kid)
    related_keywords = Keyword.objects.filter(name=keyword.name).exclude(id=kid)
    template = loader.get_template('keyword.html')
    context = {
        'campaign': campaign,
        'adgroup': adgroup,
        'keyword': keyword,
        'related_keywords': related_keywords,
    }

    return HttpResponse(template.render(context, request))

def full_table(request):
    page = 1
    num_per_page = 20

    if 'page' in request.GET and len(request.GET['page']):
        page = int(request.GET['page'])

    if 'num_per_page' in request.GET and len(request.GET['num_per_page']):
        num_per_page = int(request.GET['num_per_page'])

    if 'keyword' in request.POST and len(request.POST['keyword']):
        keyword = request.POST['keyword']
        keywords = Keyword.objects.filter(name=keyword)
    else:
        keywords = Keyword.objects.all()

    pag = pagination(round(len(keywords)/num_per_page), num_per_page, page)
    template = loader.get_template('full_table.html')
    context = {
        'keywords': keywords[(page - 1)*num_per_page:page*num_per_page],
        'pagination': pag,
    }

    return HttpResponse(template.render(context, request))

def pagination(page_number, num_per_page, page):
    prev_page = page - 1
    next_page = page + 1

    if page < 1:
        page = 1
        prev_page = 0
    elif page > page_number:
        page = page_number

    if page == page_number:
        next_page = 0

    if page_number > 10:
        if page <= 4:
            numbers = range(1, 8)
        elif page >= (page_number - 3):
            numbers = range(page_number - 6, page_number + 1)
        else:
            numbers = range(page - 3, page + 4)
    else:
        numbers = range(1, page_number + 1)

    pagination = {
        'cur_page': page,
        'first_page': 1,
        'last_page': page_number,
        'prev_page': prev_page,
        'next_page': next_page,
        'numbers': numbers
    }

    return pagination
