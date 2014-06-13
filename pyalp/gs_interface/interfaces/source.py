# needed until we don't need to vendor pgamescanner anymore
import __init__

import json
from os.path import join, dirname
import logging
import socket

from pygamescanner import source
from pygamescanner.util.proxy_transport import ProxyTransport


def query_server(address, port, get_players, get_rules):
    s = source.Source()

    addr = address, port
    s.transport = ProxyTransport(addr, s.packet_size)

    s.send_a2s_info(*addr)
    s.datagramReceived(s.transport.read(*addr), addr)
    s.send_a2s_challenge(*addr)
    s.datagramReceived(s.transport.read(*addr), addr)

    if get_players:
        logging.debug('Retrieving player data')
        s.send_a2s_player(*addr)

    if get_rules:
        logging.debug('Retrieving rule data')
        s.send_a2s_rules(*addr)

    timeouts = 10
    while timeouts > 0:
        try:
            s.datagramReceived(s.transport.read(*addr), addr)
        except socket.timeout:
            timeouts -= 1

    original_server_dict = s.server_dict[address, port]

    return {
        'mapname': original_server_dict['map'],
        'servertitle': original_server_dict['serverName'],
        'gamename': original_server_dict['gameDesc'],

        'numplayers': original_server_dict['numPlayers'],
        'maxplayers': original_server_dict['maxPlayers'],

        'password': original_server_dict['passworded'],

        'address': address,
        'hostport': original_server_dict['port'],
        'gameversion': original_server_dict['gameVersion'].split('/')[0],

        'playerkeys': {
            'score': False, 'goal': False, 'leader': False, 'enemy': False,
            'kia': False, 'roe': False, 'ping': False, 'kills': False,
            'deaths': False, 'skill': False, 'time': False, 'name': True
        },

        # simple clarifications
        'players': [json.load(
            open(join(dirname(__file__), '..', 'fake_player.json'))
        )]
    }

{
    'appid': 90,
    'challenge': 124097289,
    'dedicated': 'd',
    'edf': 145,
    'gameDesc': 'Half-Life',
    'gameDir': 'valve',
    'gameVersion': '1.1.2.2/Stdio',
    'lastTS': 1402566025.3514514,
    'latency': 'Unknown',
    'map': 'boot_camp',
    'maxPlayers': 24,
    'numBots': 0,
    'numPlayers': 0,
    'os': 'w',
    'passworded': 0,
    'players': [],
    'port': 27015,
    'secure': '\x00',
    'serverName': 'Half-Life dedicated server',
    'steamid': 90090795130889222,
    'type': 'I',
    'version': 48
}
