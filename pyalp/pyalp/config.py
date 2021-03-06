from os.path import join, exists
import importlib
import json
import logging
import warnings
from collections import OrderedDict

import dateutil.parser
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
        self.modulelist = OrderedDict()

        self.load_skin_config()
        self.load_config()

        assert isinstance(self.modulelist, OrderedDict), (
            'For ordering purposes, the module list must be an '
            'OrderedDict instance'
        )

    def load_config(self):
        path = join(settings.PROJECT_ROOT, 'pyalp', 'config.json')
        with open(path) as fh:
            contents = fh.readlines()

        config = json.loads('\n'.join(
            line
            for line in map(str.lstrip, contents)
            if not line.startswith('//')
        ))

        config.update({
            'start': dateutil.parser.parse(config['datetimestart']),
            'end': dateutil.parser.parse(config['datetimeend'])
        })
        self.config = config

    def load_skin_config(self):
        if exists(self.py_skin_config_path):
            logging.debug('Loading python config file for theme "{}"'.format(
                self.skin['skin_name']
            ))

            try:
                config = self._load_python_skin_config()
            except Exception as e:
                logging.debug('Could not load python config for {}'.format(
                    self.skin['skin_name']
                ))
                logging.exception(e)
            else:
                self.skin.update(config['skin'])
                self.modulelist.update(config['modulelist'])

        elif exists(self.php_skin_config_path):
            logging.debug('Loading php config file for theme "{}"'.format(
                self.skin['skin_name']
            ))

            try:
                config = self._load_php_skin_config()
            except Exception:
                logging.debug('Could not load php config for {} as att')
            else:
                del config['ALP_TOURNAMENT_MODE']
                self.skin.update(config)
                self.modulelist.update(config['modulelist'])

        else:
            raise Exception('Derp')

    @property
    def php_skin_config_path(self):
        return join(self.skin['skin_path'], '_config.inc.php')

    @property
    def py_skin_config_path(self):
        return join(self.skin['skin_path'], '_config.py')

    def _load_python_skin_config(self):
        module = importlib.machinery.SourceFileLoader(
            '{}.config'.format(self.skin['skin_name']),
            self.py_skin_config_path
        )
        module = module.load_module()
        assert hasattr(module, 'config')
        assert callable(module.config)

        return module.config({
            'ALP_TOURNAMENT_MODE': False
        })

    def _load_php_skin_config(self):
        warnings.warn(
            'Loading a PHP based skin configuration '
            'file is depreciated and buggy'
        )

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


def get_config():
    if not hasattr(get_config, 'config'):
        get_config.config = Config()

    return get_config.config
