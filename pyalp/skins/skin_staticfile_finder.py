from io import BytesIO
from os.path import join, splitext, split

from django.conf import settings
from django.contrib.staticfiles import utils
from django.contrib.staticfiles.finders import BaseFinder
from django.contrib.staticfiles.storage import FileSystemStorage
from django.core.files import File
from django.template.context import Context
from django.template.loader import get_template_from_string

from pyalp.skin import skin
# import pudb


class SmartFileStorage(FileSystemStorage):
    cache = {}

    def open(self, path, mode='rb'):
        """
        Renders the css template, modifies the write path
        """
        if splitext(path)[1] != '.css':
            return super().open(path, mode)

        template = self.cache.get(path, None)
        if not template:
            path = self.path(path)
            with open(path) as fh:
                data = fh.read()

            template = get_template_from_string(data, origin=path)

        context = Context({'skin': skin})
        data = template.render(context)

        data = str.encode(data, 'utf-8')
        data = BytesIO(data)
        return File(data, path)


class SkinStaticFileFinder(BaseFinder):
    storage_class = SmartFileStorage

    def __init__(self, app_names=None, *args, **kwargs):
        self.storage = self.storage_class(skin.asset_path)

        # this prefix makes django.contrib.staticfiles put the skin files in a
        # skin/ subdirectory
        # self.storage.prefix = 'skin/'

        super(SkinStaticFileFinder, self).__init__(*args, **kwargs)

    def find(self, path, all=False):
        skin_dir = join(settings.SKIN_DIR, skin.skin_name)
        file_path = join(skin_dir, path)

        if all:
            return [file_path]
        else:
            return file_path

    def list(self, ignore_patterns):
        for path in utils.get_files(self.storage, ignore_patterns):
            if split(path)[0]:
                yield path, self.storage
