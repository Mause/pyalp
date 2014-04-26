from os.path import join, exists
import importlib
import logging

from django.conf import settings

from pyalp.php_load import load_php_file

CUSTOM_LITERALS = [
    ('$colors', 'colors'),
    ('$images', 'images'),
    ('$container', 'container'),
    ('$seat', 'seat'),
    ('$container', 'container'),
    ('$modulelist', 'modulelist')
]


class Config(object):
    def __init__(self):
        self.skin = {
            'skin_name': 'default_grey'
        }
        self.skin['skin_path'] = join(
            settings.SKIN_DIR,
            self.skin['skin_name']
        )

        self.load_skin_config()

    def load_skin_config(self):

        if exists(self.php_skin_config_path):
            try:
                config = self._load_php_skin_config()
            except Exception:
                logging.debug('Could not load php config for {} as att')
            else:
                del config['ALP_TOURNAMENT_MODE']
                self.skin.update(config)

        elif exists(self.py_skin_config_path):
            import pudb
            pudb.set_trace()
            module = importlib.__import__()
            config = vars(module)

            self.skin.update(config['skin'])
        else:
            raise Exception('Derp')

    @property
    def php_skin_config_path(self):
        return join(self.skin['skin_path'], '_config.inc.php')

    @property
    def py_skin_config_path(self):
        return join(self.skin['skin_path'], '_config.py')

    def _load_php_skin_config(self):
        context = {
            'colors': {},
            'images': {},
            'container': {},
            'seat': {},
            'container': {},
            'modulelist': {},
            'ALP_TOURNAMENT_MODE': False
        }

        load_php_file(
            self.php_skin_config_path,
            context,
            custom_literals=CUSTOM_LITERALS
        )
        return context

config = Config()
