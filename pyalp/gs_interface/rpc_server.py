# needed until we don't need to vendor tinyrpc anymore
from __init__ import init, KEYS_DIR
init()

from os.path import join, dirname
import glob
import logging
import os
import sys

import zmq
from zmq.auth.thread import ThreadAuthenticator as Authenticator

from threaded import RPCServerThreaded as RPCServer
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.zmq import ZmqServerTransport

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zmq.auth').setLevel(logging.WARNING)

HERE = dirname(__file__)


# standalong scripts need extra setup
from configurations import importer
os.environ.update({
    'DJANGO_CONFIGURATION': 'Dev',  # setting doesn't really matter
    'DJANGO_SETTINGS_MODULE': 'pyalp.settings'
})
importer.install(check_options=True)
sys.path.insert(0, join(HERE, '..'))


def setup_auth(ctx):
    """
    Creates an Authenticator instance correctly configured
    for "ironhouse" authentication.

    word of warning; if the return value from this function ever gets garbage
    collected, the authenticator will get shut down, and authentication will
    obviously cease to function
    """

    # Start an authenticator for this context.
    auth = Authenticator(ctx, log=logging.getLogger('zmq.auth'))
    auth.start()
    # auth.allow('127.0.0.1')

    # Tell the authenticator how to handle CURVE requests
    assert glob.glob(join(KEYS_DIR, '*.key'))
    auth.configure_curve(domain='*', location=KEYS_DIR)

    return auth


def setup_server(end_point):
    ctx = zmq.Context.instance()
    auth = setup_auth(ctx)

    socket = ctx.socket(zmq.ROUTER)

    socket.curve_publickey, socket.curve_secretkey = (
        zmq.auth.load_certificate(
            join(KEYS_DIR, "server.key_secret")
        )
    )

    socket.curve_server = True  # must come before bind
    socket.bind(end_point)

    server = ZmqServerTransport(socket)
    server.auth = auth

    return server


def main():
    import rpc_server_methods

    transport = setup_server('tcp://*:5001')
    rpc_server = RPCServer(
        transport,
        JSONRPCProtocol(),
        rpc_server_methods.dispatcher
    )

    logging.info("RPC server will serve forever")

    # enter an infinite loop
    rpc_server.serve_forever()


def test():
    import rpc_server_methods

    import time
    start = time.time()
    response = rpc_server_methods.query_server(
        # 'hlife2',
        'gamespy2',
        '192.168.1.104',

        # '27015',
        '2302',

        False,
        False
    )
    print(time.time() - start)

    from pprint import pprint
    pprint(response)

if __name__ == '__main__':
    # test()
    main()
