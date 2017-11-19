import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fake_generator = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        topic = add_topic()
        
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()
        fake_name = fake_generator.company()
        
        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating scripts")
    populate(20)
    print("Population complete!")