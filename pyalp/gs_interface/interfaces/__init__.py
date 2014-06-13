from os.path import join, exists, isdir
from django.conf import settings

pygamescanner_dir = join(
    settings.PROJECT_ROOT,
    '..',
    'pyGameScanner',
)

assert exists(pygamescanner_dir) and isdir(pygamescanner_dir)

import sys
sys.path.insert(0, pygamescanner_dir)


from . import source, hlife2, gamespy2, halo
source, hlife2, gamespy2, halo
