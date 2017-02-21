from django.conf import settings
from django.db import models
from temba_client.v2 import TembaClient
__author__ = 'kenneth'


class Group(models.Model):
    uuid = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    query = models.CharField(max_length=100, blank=True, null=True)
    count = models.IntegerField()

    @classmethod
    def add_groups(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        groups = client.get_groups().all()
        added = 0
        for group in groups:
            if not cls.group_exists(group):
                cls.objects.create(uuid=group.uuid, name=group.name, query=group.query, count=group.count)
                added += 1

        return added

    @classmethod
    def group_exists(cls, group):
        return cls.objects.filter(uuid=group.uuid).exists()