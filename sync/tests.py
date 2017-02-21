from django.test import TestCase
from models import Group

__author__ = 'kenneth'


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