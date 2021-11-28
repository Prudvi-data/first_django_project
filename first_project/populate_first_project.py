#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic

from faker import Faker

fakegen = Faker()

topics = ['Social','Science','Neurology','AIDS','Sexology']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get the topic for entry

        top = add_topic()

        #create fake data for that entry

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new WebPage entry

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create the new AccessRecord entry

        acc_rec = AccessRecord.objects.get_or_create(date=fake_date,name=webpg)[0]


if __name__ == '__main__' :
    print("Populating Script")
    populate(10)
    print("Script Populated")
