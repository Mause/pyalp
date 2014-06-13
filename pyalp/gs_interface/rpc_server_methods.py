import logging
import importlib
from os import listdir
from os.path import splitext, join, dirname
import socket

from tinyrpc.dispatch import RPCDispatcher
HERE = dirname(__file__)


dispatcher = RPCDispatcher()


@dispatcher.public
def protocol_exists(protocol_name):
    logging.info('Protocol exists request for {}'.format(
        protocol_name
    ))

    filenames = listdir(
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
