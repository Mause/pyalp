from os.path import join
import json
from collections import defaultdict

from django.conf import settings

# from flags.models import Flag


# def get_statusdict():
#     d = defaultdict(lambda: False)
#     d.update({
#         flag.name: flag.enabled
#         for flag in Flag.objects.all()
#     })
#     return d

def get_statusdict():
    d = defaultdict(lambda: False)
    with open(join(settings.PROJECT_ROOT, 'pyalp', 'flags.json')) as fh:
        d.update(json.load(fh))

    return d


def get_flag_registry():
    return type('flag_registry', (object,), {
        'get_statusdict': get_statusdict
    })
