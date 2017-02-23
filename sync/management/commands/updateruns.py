from django.core.management import BaseCommand
from sync.models import Run


class Command(BaseCommand):
    def handle(self, *args, **options):
        added_runs = Run.add_runs()
        self.stdout.write(self.style.SUCCESS('Successfully added %d steps' % added_runs))