import os
from typing import _T_co

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

#SQL verison 'select * from Topic'
topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    print(topic.text)
    #print(topic) - defined string function returning the text
    print(topic.date_added)

t = Topic.objects.get(id=1)
print(t)

entries = t.entry_set.all()

for e in entries:
    print(e)