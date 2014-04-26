#main/contexts.py
from django.core.urlresolvers import resolve

from cl_module.cl_module import ModuleManager


def app_name(request):
    return {'app_name': resolve(request.path).app_name}


def url_name(request):
    return {'url_name': resolve(request.path).url_name}


def skin(request):
    from pyalp.skin import skin
    return {'skin': skin}


def modules(request):
    return {'modules': ModuleManager()}


def lan(request):
    # TODO: have this load info from the db instead
    lan = {'name': 'RFLAN'}

    return {'lan': lan}
