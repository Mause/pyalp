#main/contexts.py
from os.path import join
import json

from django.core.urlresolvers import resolve
from django.conf import settings

from cl_module.cl_module import ModuleManager
from flags.registry import get_flag_registry
from skins import get_skin


def app_name(request):
    return {'app_name': resolve(request.path).app_name}


def url_name(request):
    return {'url_name': resolve(request.path).url_name}


def skin(request):
    return {'skin': get_skin()}


def modules(request):
    return {'modules': ModuleManager()}


def lan(request):
    return {'lan': get_config().config}


def current_security_level(request):
    from pyalp.security import current_security_level as csl

    return {'current_security_level': csl(request.user)}


def flags(request):
    return {'flags': get_flag_registry().get_statusdict()}
