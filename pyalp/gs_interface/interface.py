from os.path import join, dirname
HERE = dirname(__file__)

import logging
from apps.tournaments.models import Server, GameRequest
from .rpc_client import get_interface
import yaml


resource_load = lambda name: yaml.load(open(
    join(HERE, 'resources', name)
))

game_ports = resource_load('game_ports.yaml')
game_names = resource_load('game_names.yaml')

interface = get_interface()


class NonExistantProtocol(Exception):
    pass


class CouldNotReachServer(Exception):
    pass


def calcqport(port, qgame):
    assert qgame, qgame
    assert qgame in game_ports, "Game Type not a valid type: {}".format(qgame)

    portdiff = game_ports[qgame]

    # check out value:
    if portdiff[0] == '+':  # if it starts with a + or -, it's an offset.
        return port + int(portdiff[1:])

    elif portdiff[0] == '-':  # if it's 0, it means no change.
        return port - int(portdiff[1:])

    elif portdiff[0] == '0':  # anything else is a static port.
        return port

    else:
        return portdiff


def _query_server(
        serv, address, port, protocol, get_players=False, get_rules=False):

    qport = calcqport(port, serv.game.short)
    if qport is False:  # zero could be returned and eval'd as False
        print("Unable to calculate query port for address")
    else:
        port = qport

    logging.debug(port, "==>", qport)
    logging.debug("querying {}:{} over the {} protocol".format(
        address, port, protocol
    ))

    if not interface.protocol_exists(protocol):
        raise NonExistantProtocol(protocol)

    return interface.query_server(
        protocol,
        address,
        port,
        get_players,
        get_rules
    )


def queryServer(address, port, protocol, get_players=False, get_rules=False):
    logging.info('queryServer request for {}:{} for {}'.format(
        address, port, protocol
    ))

    result = Server.objects.filter(
        ipaddress=address, game__querystr2=protocol
    ).select_related('game')

    if not result:
        result = GameRequest.objects.filter(
            ipaddress=address, game__querystr2=protocol
        )

    if not result:
        raise CouldNotReachServer(
            '{}:{} with protocol {}'.format(address, port, protocol)
        )

    return _query_server(
        address, port, protocol,
        get_players, get_rules
    )


def query_server_from_instance(serv, get_players=False, get_rules=False):
    return _query_server(
        serv,
        serv.address,
        serv.queryport,
        serv.game.engine_type,
        get_players,
        get_rules
    )


def game_title(gamename):
    gamename = gamename.lower()

    try:
        return game_names[gamename]
    except KeyError:
        return "Game Status"
