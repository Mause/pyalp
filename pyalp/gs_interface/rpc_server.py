# needed until we don't need to vendor tinyrpc anymore
from __init__ import init
# from __init__ import KEYS_DIR
init()

from os.path import join, dirname, splitext
import importlib
import logging
import os
import socket
import sys

import zmq

from threaded import RPCServerThreaded as RPCServer
from tinyrpc.dispatch import RPCDispatcher
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.zmq import ZmqServerTransport

# from rpc_common import setup_auth

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zmq.auth').setLevel(logging.DEBUG)

HERE = dirname(__file__)


# standalong scripts need extra setup
from configurations import importer
os.environ.update({
    'DJANGO_CONFIGURATION': 'Dev',
    'DJANGO_SETTINGS_MODULE': 'pyalp.settings'
})
importer.install(check_options=True)
sys.path.insert(0, join(HERE, '..'))


dispatcher = RPCDispatcher()


@dispatcher.public
def protocol_exists(protocol_name):
    logging.info('Protocol exists request for {}'.format(
        protocol_name
    ))

    filenames = os.listdir(
        join(HERE, 'interfaces')
    )

    filenames = {
        splitext(filename)[0].lower()
        for filename in filenames
        if filename != '__init__.py'
    }

    return protocol_name.lower() in filenames


@dispatcher.public
def query_server(protocol, address, port, get_players, get_rules):
    logging.info('Query server request for stat on {}:{}'.format(
        address, port
    ))

    assert protocol_exists(protocol), 'No such protocol'
    protocol = importlib.import_module('interfaces.{}'.format(protocol))

    try:
        return protocol.query_server(
            address, port, get_players, get_rules
        )

    except socket.timeout as e:
        raise socket.timeout('{}: could not reach {}:{}'.format(
            e, address, port
        ))

    except Exception as e:
        logging.exception(e)
        raise

    finally:
        logging.info('request complete')


def setup_server(end_point):
    ctx = zmq.Context.instance()
    # auth = setup_auth(ctx)

    socket = ctx.socket(zmq.ROUTER)

    # socket.curve_publickey, socket.curve_secretkey = (
    #     zmq.auth.load_certificate(
    #         join(KEYS_DIR, 'server', "server.key_secret")
    #     )
    # )

    # socket.curve_server = True  # must come before bind
    socket.bind(end_point)

    server = ZmqServerTransport(socket)
    # server.auth = auth

    return server


def main():
    transport = setup_server('tcp://*:5001')
    rpc_server = RPCServer(
        transport,
        JSONRPCProtocol(),
        dispatcher
    )

    logging.info("RPC server will serve forever")

    rpc_server.serve_forever()


def test():
    import time
    start = time.time()
    response = query_server(
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
