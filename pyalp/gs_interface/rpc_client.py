# needed until we don't need to vendor tinyrpc anymore
from . import init, KEYS_DIR
init()
from os.path import join

import zmq
import zmq.auth

from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.zmq import ZmqClientTransport
from tinyrpc import RPCClient

import logging
logging.basicConfig(level=logging.DEBUG)

logging.getLogger('zmq.auth').setLevel(logging.DEBUG)


def setup_client(end_point):
    logging.info('Setting up client')

    ctx = zmq.Context.instance()

    socket = ctx.socket(zmq.REQ)
    socket.curve_publickey, socket.curve_secretkey = zmq.auth.load_certificate(
        join(KEYS_DIR, "client.key_secret")
    )
    # The client must know the server's public key to make a CURVE connection.
    socket.curve_serverkey, _ = zmq.auth.load_certificate(
        join(KEYS_DIR, "server.key")
    )

    socket.connect(end_point)

    client = RPCClient(
        JSONRPCProtocol(),
        ZmqClientTransport(socket)
    )

    return client


def get_interface():
    if not hasattr(get_interface, '_interface'):

        client = setup_client('tcp://127.0.0.1:5001')

        get_interface._interface = client.get_proxy()

    return get_interface._interface


def main():
    logging.info('Lets go!')
    q = setup_client('tcp://127.0.0.1:5001')
    logging.info('Trying')

    print(q.batch_call([
        ('protocol_exists', ['halo']),
        ('protocol_exists', ['gamespy']),
        ('query_server', ['halo', '192.168.1.104', '27015', False, False])
    ]))

if __name__ == '__main__':
    main()
