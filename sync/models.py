from django.conf import settings
from django.db import models
from temba_client.v2 import TembaClient
from django.utils import timezone


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


class Run(models.Model):

    id = models.IntegerField(primary_key=True)
    flow = models.CharField(max_length=200, default='flow')
    contact = models.CharField(max_length=200, default='contact')
    responded = models.BooleanField()
    path = models.CharField(max_length=200, null=True)
    values = models.CharField(max_length=200, null=True)
    created_on = models.DateTimeField(default=timezone.now())
    modified_on = models.DateTimeField(null=True)
    exited_on = models.DateTimeField(null=True)
    exit_type = models.CharField(max_length=200, null=True, default=None)

    @classmethod
    def add_runs(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        runs = client.get_runs().all()
        added_runs = 0
        for run in runs:
            if not cls.run_exists(run):
                cls.objects.create(id=run.id, flow=run.flow, contact=run.contact, responded=run.responded,
                                   path=run.path, values=run.values,
                                   created_on=run.created_on, modified_on=run.modified_on, exited_on=run.exited_on,
                                   exit_type=run.exit_type)
                #for this_step in run.path:
                #   Step.add_steps(this_step.node, this_step.time, run.id)
                for this_value in run.values:
                    Value.add_values(this_value.value, this_value.category, this_value.node, this_value.time, run.id)
                added_runs += 1

        return added_runs

    @classmethod
    def run_exists(cls, run):
        return cls.objects.filter(id=run.id).exists()


class Step(models.Model):
    node = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())
    run_id = models.ForeignKey(Run, default=None)

    @classmethod
    def add_steps(cls, node, time, run_id):
        cls.objects.create(node=node, time=time, run_id=run_id)


class Value(models.Model):
    value = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    node = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())
    run_id = models.ForeignKey(Run, default=None)

    @classmethod
    def add_values(cls, value, category, node, time, run_id):
        cls.objects.create(value=value, category=category, node=node, time=time, run_id=run_id)
