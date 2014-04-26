from os.path import join

from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirLoader

from pyalp.skin import skin
skin_template_dir = join(settings.SKIN_DIR, skin.skin_name)


class Loader(AppDirLoader):
    is_usable = True

    def get_template_sources(self, template_name, template_dirs=None):
        return super().get_template_sources(template_name, [skin_template_dir])
