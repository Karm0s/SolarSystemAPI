import os

from django.core.management.base import BaseCommand, CommandError
from core.models import CelestialBody
from openpyxl import load_workbook

class Command(BaseCommand):
    help = 'Populate DataBase with data extracted from excel sheet'

    def add_arguments(self, parser):
        parser.add_argument('excel_sheet', type=str)
    
    def handle(self, *args, **kwargs):
        file = kwargs['excel_sheet']
        
        wb = load_workbook(os.path.join(os.environ.get('SOLARSYSTEMAPI_ROOT'), file))

        self.stdout.write(str(wb.get_sheet_names()), ending='')