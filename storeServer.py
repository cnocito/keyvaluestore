__author__ = 'cnocito'

import asyncio
from store import Store, Response
import time

class DbInstance(asyncio.Protocol):
    store = Store()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        response = Response()
        response.SetError()
        elements = data.decode('UTF-8').split('\n')
        if len(elements) == 2:
            elements = data.decode('UTF-8').strip('\r\n').split('\t')
            action = elements[0]
            if action == 'get':
                if len(elements) == 2:
                    start = time.time()
                    key = elements[1]
                    value = self.store.get(key)
                    end = time.time()
                    elapsed_time = end - start
                    response.SetSuccess(time=elapsed_time, value=value)
            elif action == 'put':
                if len(elements) == 3:
                    start = time.time()
                    key = elements[1]
                    value = elements[2]
                    self.store.put(key, value)
                    end = time.time()
                    elapsed_time = end - start
                    response.SetSuccess(time=elapsed_time, value=value)
            elif action == 'delete':
                if len(elements) == 2:
                    start = time.time()
                    key = elements[1]
                    self.store.delete(key)
                    end = time.time()
                    elapsed_time = end - start
                    response.SetSuccess(time=elapsed_time, value="")
            else:
                response.SetError()
            self.transport.write(bytes((str(response.__dict__)+'\n').encode('UTF-8')))

loop = asyncio.get_event_loop()
server = loop.run_until_complete(loop.create_server(DbInstance, '127.0.0.1', 4444))
loop.run_forever()