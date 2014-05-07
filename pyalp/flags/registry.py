from flags.models import Flag
from collections import defaultdict


def get_statusdict():
    d = defaultdict(lambda: False)
    d.update({
        flag.name: flag.enabled
        for flag in Flag.objects.all()
    })
    return d


def get_flag_registry():
    return type('flag_registry', (object,), {
        'get_statusdict': get_statusdict
    })
