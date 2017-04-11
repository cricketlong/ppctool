from django.http import HttpResponse
from django.template import loader
from .models import Campaign, AdGroup, Keyword

def index(request):
    campaigns = Campaign.objects.all()
    template = loader.get_template('index.html')
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
    keywords = Keyword.objects.all()
    template = loader.get_template('full_table.html')
    context = {
        'keywords': keywords,
    }

    return HttpResponse(template.render(context, request))
