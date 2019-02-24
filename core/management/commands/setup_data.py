from django.core.management.base import BaseCommand
from easy_eats.data_populate import PopulateData


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        ob = PopulateData()
        print("Creating Tags")
        ob.populate_tags()
        print("Creating Users")
        ob.populate_user()
        print("Creating Resturants")
        ob.populate_resturants()
