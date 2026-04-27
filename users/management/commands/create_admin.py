from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Cria um usuário administrador'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'Usuário "{username}" já existe.'))
            return

        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        user.role = 'admin'
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Admin "{username}" criado com sucesso.'))
