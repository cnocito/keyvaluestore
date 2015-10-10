__author__ = 'cnocito'

class Store:
    db = {}
    count = 0

    def get(self, key):
        try:
            return self.db[key]
        except:
            return ""

    def put(self, key, value):
        try:
            self.db[key] = value
            self.count += 1
            return True
        except:
            return False

    def delete(self, key):
        try:
            self.db.pop(key)
            self.count -= 1
            return True
        except:
            return False

class Response(dict):
    execution = False
    time = 0
    value = ''

    def SetError(self):
        self.execution = False
        self.time = 0
        self.value = ''

    def SetSuccess(self, time, value):
        self.execution = True
        self.time = time
        self.value = value
