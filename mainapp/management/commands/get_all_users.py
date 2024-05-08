from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f'Пользователь - {user}')