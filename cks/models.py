from django.db import models

class Campaign(models.Model):
    class Meta:
        db_table = "campaign"

    id = models.IntegerField(primary_key = True, default = 0)
    name = models.CharField(max_length = 255)
    
class AdGroup(models.Model):
    class Meta:
        db_table = "ad_group"

    id = models.IntegerField(primary_key = True, default = 0)
    name = models.CharField(max_length = 255)
    campaign = models.ForeignKey(Campaign)

class Keyword(models.Model):
    class Meta:
        db_table = "keyword"

    id = models.IntegerField(primary_key = True, default = 0)
    campaign = models.ForeignKey(Campaign)
    adgroup = models.ForeignKey(AdGroup)
    name = models.CharField(max_length = 255)
    bid = models.FloatField(default=0.0)
    impressions = models.IntegerField(default=0.0)
    clicks = models.IntegerField(default=0.0)
    order_amount_first_month = models.FloatField(default=0.0)
