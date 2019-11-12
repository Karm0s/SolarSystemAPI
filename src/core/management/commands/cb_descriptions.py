import os

from django.core.management.base import BaseCommand
from core.models import CelestialBody

class Command(BaseCommand):
    help = 'Add description to the celestial bodies'

    def add_arguments(self, parser):
        parser.add_argument('cb_descriptions', type=str)
    
    def handle(self, *args, **options):
        
        file = os.path.join(os.environ.get('SOLARSYSTEMAPI_ROOT'), options['cb_descriptions'])

        with open(file, 'r') as f:
            for line in f.readlines():
                name, description = line.split('|')
                body = CelestialBody.objects.get(name=name)
                body.description = description
                body.save()
                print(body.description)