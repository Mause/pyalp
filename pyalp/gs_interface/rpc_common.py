import logging
from os.path import join

from zmq.auth.thread import ThreadAuthenticator as Authenticator
import zmq

try:
    from __init__ import KEYS_DIR
except ImportError:
    from . import KEYS_DIR


stonehouse = False


def setup_auth(ctx, client=False):
    # Start an authenticator for this context.
    auth = Authenticator(ctx, log=logging.getLogger('zmq.auth'))
    auth.start()

    if not client:
        auth.allow('127.0.0.1')

    # Tell the authenticator how to handle CURVE requests
    if stonehouse:
        location = zmq.auth.CURVE_ALLOW_ANY

    else:
        # else ironhouse
        location = join(KEYS_DIR, 'public_keys')

    auth.configure_curve(domain='*', location=location)

    return auth
