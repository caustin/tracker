from django.db import models


class License(models.Model):

    name = models.TextField()
    brief_description = models.TextField()
    url = models.URLField()
    acceptable = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class ThirdPartyComponent(models.Model):

    name = models.TextField()
    license = models.ForeignKey('License')
    download_link = models.URLField()
    version = models.CharField(max_length=100)
    documentation_link = models.URLField()

    def __unicode__(self):
        return self.name