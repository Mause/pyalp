from os.path import join

from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirLoader

from . import get_skin


class Loader(AppDirLoader):
    is_usable = True

    def __init__(self, *args, **kwargs):
        skin = get_skin()

        self.skin_template_dir = join(
            settings.SKIN_DIR,
            skin.skin_name
        )

    def get_template_sources(self, template_name, template_dirs=None):
        return super().get_template_sources(
            template_name, [self.skin_template_dir]
        )
