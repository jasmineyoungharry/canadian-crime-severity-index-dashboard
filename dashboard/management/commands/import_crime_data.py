import csv
from django.core.management.base import BaseCommand
from dashboard.models import CrimeRecord


class Command(BaseCommand):
    help = 'Import crime data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        CrimeRecord.objects.all().delete()
        count = 0

        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            for row in reader:
                year = row.get('REF_DATE')
                geography = row.get('GEO')
                metric = row.get('Statistics')
                value = row.get('VALUE')

                if not year or not geography or not metric or not value:
                    continue

                try:
                    CrimeRecord.objects.create(
                        province_or_territory=geography.strip(),
                        year=int(float(year)),
                        metric=metric.strip(),
                        value=float(value)
                    )
                    count += 1
                except ValueError:
                    continue

        self.stdout.write(self.style.SUCCESS(
            f'Crime data imported successfully. {count} records added.'
        ))