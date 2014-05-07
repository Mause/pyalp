import os

from pyalp.php_load import load_lang_file

locale_data = os.path.join(os.path.dirname(__file__), '..', 'locale_data')

lang = load_lang_file(os.path.join(locale_data, 'en.php'))
# lang = load_lang_file(os.path.join(locale_data, 'fr.php'))


# this is really just one way of doing things; another would be via
# a closure, but meh
class GetTexter(object):
    def __init__(self, context_name):
        self.context_name = context_name

    def get_via_explicit_context(self, path):
        explicit_context_name, const_name = path.split('.')

        context = lang[explicit_context_name]
        return context[const_name]

    def __call__(self, path):
        if '.' in path:
            return self.get_via_explicit_context(path)

        try:
            return lang[self.context_name][path]
        except KeyError:
            pass

        try:
            return lang['global'][path]
        except KeyError:
            return path


def custom_gettext(context_name):
    return GetTexter(context_name)


def gettext(context_name, path):
    return custom_gettext(context_name)(path)
