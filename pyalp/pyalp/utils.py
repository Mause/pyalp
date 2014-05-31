from itertools import chain, repeat

from django.template import RequestContext
from django.shortcuts import render_to_response as _rtr
from django.views.generic import RedirectView


redirect = lambda url: RedirectView.as_view(url=url)


def render_to_response(*args, **kwargs):
    """
    Wraps django.shortcuts.render_to_response to ensure that
    a the request context is passed through
    """

    assert 'context_instance' in kwargs, 'a context_instance is required!'
    kwargs['context_instance'] = RequestContext(
        kwargs['context_instance']
    )

    return _rtr(*args, **kwargs)


def split_contents(ttoken, expected):
    tokens = ttoken.split_contents()
    tokens = tokens[1:]  # rid ourselves of the name

    extension = expected - len(tokens)
    extension = repeat(None, extension)

    return chain(tokens, extension)
