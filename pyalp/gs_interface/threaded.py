#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from init import init
init()

from tinyrpc.server import RPCServer
import concurrent.futures


class RPCServerThreaded(RPCServer):
    def __init__(self, *args, **kw):
        self.executor = concurrent.futures.ThreadPoolExecutor(5)

        return RPCServer.__init__(self, *args, **kw)

    def _spawn(self, func, *args, **kwargs):
        self.executor.submit(func, *args, **kwargs)
