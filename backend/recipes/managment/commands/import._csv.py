import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredients


class Command(BaseCommand):
    help = 'Импорт ингредиентов из CSV'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Расположение CSV')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ingredient = Ingredients(
                    name=row[0],
                    measurement_unit=row[1],
                )
                ingredient.save()

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
