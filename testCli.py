__author__ = 'cnocito'

import sys
import traceback
import storeClient
import time

if len(sys.argv) < 2:
    print("Invalid number of arguments!")
else:
    try:
        client = storeClient.StoreClient()
        client.connect()
        action = sys.argv[1]
        start = time.time()
        if action == 'get':
            client.get(sys.argv[2])
        elif action == 'put':
            client.put(sys.argv[2],sys.argv[3])
        elif action == 'update':
            client.put(sys.argv[2],sys.argv[3])
        elif action == 'delete':
            client.delete(sys.argv[2])
        end = time.time()
        print(end-start)
    except:
        print(traceback.format_exc())
