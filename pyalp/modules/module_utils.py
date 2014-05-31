from importlib import import_module

from django.conf import settings
from django.utils.module_loading import module_has_submodule

from django.template.base import import_library, get_templatetags_modules


libraries = {}


class InvalidTemplateLibrary(Exception):
    pass


class ModuleLibrary(object):
    def __init__(self):
        self.modules = {}

    def module(self, name=None, compile_function=None):
        if name is None and compile_function is None:
            # @register.module()
            return self.module_function
        elif name is not None and compile_function is None:
            if callable(name):
                # @register.module
                return self.module_function(name)
            else:
                # @register.module('somename') or
                # @register.module(name='somename')
                def dec(func):
                    return self.module(name, func)
                return dec
        elif name is not None and compile_function is not None:
            # register.module('somename', somefunc)
            self.modules[name] = compile_function
            return compile_function
        else:
            raise InvalidTemplateLibrary(
                "Unsupported arguments to "
                "Library.module: (%r, %r)", (name, compile_function)
            )

    def module_function(self, klass):
        self.modules[klass.module_name] = klass
        return klass


def is_library_missing(name):
    """Check if library that failed to load cannot be found under any
    templatetags directory or does exist but fails to import.

    Non-existing condition is checked recursively for each subpackage in cases
    like <appdir>/templatetags/subpackage/package/module.py.
    """
    # Don't bother to check if '.' is in name since any name will be prefixed
    # with some template root.
    path, module = name.rsplit('.', 1)
    try:
        package = import_module(path)
        return not module_has_submodule(package, module)
    except ImportError:
        return is_library_missing(path)


def get_modules():
    """
    Return the list of all available template tag modules.

    Caches the result for faster access.
    """
    if not hasattr(get_templatetags_modules, 'templatetags_modules'):
        _modules = []
        # Populate list once per process. Mutate the local list first, and
        # then assign it to the global name to ensure there are no cases
        # where two threads try to populate it simultaneously.
        for app_module in settings.INSTALLED_APPS:
            try:
                module = '%s.modules' % app_module
                import_module(module)
                _modules.append(module)
            except ImportError:
                continue

        get_modules.templatetags_modules = _modules

    return get_modules.templatetags_modules


def get_module_library(library_name):
    """
    Load the template library module with the given name.

    If library is not already loaded loop over all templatetags modules
    to locate it.

    {% load somelib %} and {% load someotherlib %} loops twice.

    Subsequent loads eg. {% load somelib %} in the same process will grab
    the cached module from libraries.
    """
    lib = libraries.get(library_name, None)
    if not lib:
        templatetags_modules = get_modules()
        tried_modules = []

        for module in templatetags_modules:
            taglib_module = '%s.%s' % (module, library_name)
            tried_modules.append(taglib_module)
            lib = import_library(taglib_module)
            if lib:
                libraries[library_name] = lib
                break
        if not lib:
            raise InvalidTemplateLibrary(
                "Template library {} not found, tried {}".format(
                    library_name, ','.join(tried_modules)
                )
            )
    return lib
