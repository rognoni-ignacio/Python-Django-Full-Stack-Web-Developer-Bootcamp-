import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from second_app.models import User
from faker import Faker

fake_generator = Faker()


def populate(N=5):
    for entry in range(N):

        fake_first_name = fake_generator.first_name()
        fake_last_name = fake_generator.last_name()
        fake_email = fake_generator.free_email()

        user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating scripts")
    populate(20)
    print("Population complete!")
