__author__ = 'cnocito'

import socket

class StoreClient:
    address = ''
    port = 0
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address='', port=4444):
        self.address = address
        self.port = port

    def connect(self):
        self.conn.connect((self.address, self.port))

    def communicate(self, message):
        try:
            self.conn.sendall(bytes(message.encode('UTF-8')))
            buff = bytes()
            while True:
                buff += self.conn.recv(1024)
                if buff.decode('UTF-8').find('\n') != -1:
                    return buff.decode('UTF-8')
        except:
            return False

    def test(self):
        try:
            message = '1234' + '\t' + '1234' + '\n'
            self.conn.sendall(bytes(message.encode('UTF-8')))
            buff = bytes()
            while True:
                buff += self.conn.recv(1024)
                if buff.decode('UTF-8').find('\n') != -1:
                    return buff.decode('UTF-8')
        except:
            return False

    def put(self, key, value):
        message = "put" + "\t" + key + "\t" + value + "\n"
        return self.communicate(message)

    def get(self, key):
        message = "get" + "\t" + key + "\n"
        return self.communicate(message)

    def update(self, key, value):
        message = "udpate" + "\t" + key + "\t" + value + "\n"
        return self.communicate(message)

    def delete(self, key):
        message = "delete" + "\t" + key + "\n"
        return self.communicate(message)

    def __del__(self):
        self.conn.close()
