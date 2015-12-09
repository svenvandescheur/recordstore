from django.core.management.base import BaseCommand

from core.models import Release


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        """
        Searches for information by by barcode
        Passes first matched result to process_result()
        """
        releases = Release.objects.all()

        for release in releases:
            release.collect_info()
