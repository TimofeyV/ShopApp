from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Get all users"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'Пользователь с ID {pk} - {user}')
