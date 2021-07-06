from django.core.management.base import BaseCommand

from groups.models import Group


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=int, dest='args')

    def handle(self, *args, **options):
        Group.generate_groups(args[0])
