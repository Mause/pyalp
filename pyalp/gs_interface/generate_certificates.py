#!/usr/bin/env python

"""
Generate client and server CURVE certificate files then move them into the
appropriate store directory, private_keys or public_keys. The certificates
generated by this script are used by the stonehouse and ironhouse examples.

In practice this would be done by hand or some out-of-band process.

Author: Chris Laws
"""

import zmq.auth

from __init__ import KEYS_DIR


def generate_certificates():
    ''' Generate client and server CURVE certificate files'''

    # create new keys in certificates dir
    zmq.auth.create_certificates(KEYS_DIR, "server")
    zmq.auth.create_certificates(KEYS_DIR, "client")

if __name__ == '__main__':
    generate_certificates()
