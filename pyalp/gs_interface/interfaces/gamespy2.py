
from pygamescanner.util.proxy_transport import ProxyTransport
from pygamescanner.gamespy2 import GameSpy2


def query_server(address, port, get_players, get_rules):
    s = GameSpy2()

    s.transport = ProxyTransport((address, port), s.packet_size)

    s.send_status_query(address, port)

    return s.datagramReceived(
        s.transport.read(address, port),
        (address, port)
    )
