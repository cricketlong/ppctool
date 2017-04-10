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

class Keyword(models.Model):
    class Meta:
        db_table = "keyword"

    id = models.IntegerField(primary_key = True, default = 0)
    campaign = models.ForeignKey(Campaign)
    ad_group = models.ForeignKey(AdGroup)
    name = models.CharField(max_length = 255)
    bid = models.FloatField(default=0.0)
