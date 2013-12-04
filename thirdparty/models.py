from django.db import models


class License(models.Model):

    name = models.TextField()
    brief_description = models.TextField()
    url = models.URLField()
    acceptable = models.BooleanField(default=False)
    thirdpartycomponents = models.ManyToManyField('ThirdPartyComponent')

    def __unicode__(self):
        return self.name


class Component(models.Model):

    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    unique_together = ('name', 'version')

    def __unicode__(self):
        return "{0:s}, {1:s}".format(self.name, self.version)


class ThirdPartyComponent(models.Model):

    name = models.TextField()
    download_link = models.URLField()
    version = models.CharField(max_length=100)
    documentation_link = models.URLField()
    component = models.ForeignKey('Component', null=True)

    def __unicode__(self):
        return self.name


class Vulnerability(models.Model):

    description = models.TextField()
    remediation = models.TextField()
    remediated = models.BooleanField(default=False)

    def __unicode__(self):
        return self.description[:10]
