from django.core.management.base import BaseCommand

import cryptography.fernet
from six import PY2


class Command(BaseCommand):
    help = 'Generates a new Fernet encryption key'

    def handle(self, *args, **options):
        key = cryptography.fernet.Fernet.generate_key()
        if PY2:
            self.stdout.write(key.decode())
        else:
            self.stdout.write(key.decode('utf-8'), ending='\n')
