from django.test import TestCase
from models import Group, Run
from django.utils import timezone


class TestGroup(TestCase):
    def test_add_groups(self):
        group_count = Group.objects.count()
        added_groups = Group.add_groups()
        self.assertEquals(Group.objects.count(), group_count + added_groups)

    def test_group_exists(self):
        class G(object):
            def __init__(self, name=None, uuid=None, query=None, count=None):
                self.name = name
                self.uuid = uuid
                self.query = query
                self.count = count

        rapidpro_mock_group = G(name='Test Group', uuid='random number', query=None, count=4)
        self.assertEquals(Group.group_exists(rapidpro_mock_group), False)
        Group.objects.create(name='Test Group', uuid='random number', query=None, count=4)
        self.assertEquals(Group.group_exists(rapidpro_mock_group), True)


class TestRun(TestCase):
    def test_add_runs(self):
        run_count = Run.objects.count()
        added_runs = Run.add_runs()
        self.assertEquals(Run.objects.count(), run_count + added_runs)

    def test_run_exists(self):
        class S(object):
            def __init__(self, run_id=None, flow=None, contact=None, responded=None, path=None, values=None, created_on=None, modified_on=None,
                         exited_on=None, exit_type=None):
                self.id = run_id
                self.flow = flow
                self.contact = contact
                self.responded = responded
                self.path = path
                self.values = values
                self.created_on = created_on
                self.modified_on = modified_on
                self.exited_on = exited_on
                self.exit_type = exit_type

        rapidpro_mock_run = S(run_id=1, flow='Test flow', contact='Test contact', responded=1, path='Test path',
                              values='Test Values', created_on=timezone.now(),
                              modified_on=None, exited_on=None, exit_type='Test exit_type')
        self.assertEquals(Run.run_exists(rapidpro_mock_run), False)
        Run.objects.create(id=1, flow='Test flow', contact='Test contact', responded=1, path='Test path',
                           values='Test Values', created_on=timezone.now(),
                           modified_on=None, exited_on=None, exit_type='Test exit_type')
        self.assertEquals(Run.run_exists(rapidpro_mock_run), True)
