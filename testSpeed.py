__author__ = 'cnocito'

from store import Store
import uuid
import time
import storeClient
import numpy as np
import pandas as pd

keys = []
nElements = 1000000
times = []

print("*** Testing performance on %s elements ***" % nElements)
print("\nData Structure and Store Testing (no network or concurrency)")
# Measure time to generate a hash
start = time.time()
for i in range(0, nElements - 1):
    k = str(uuid.uuid1())
    keys.append(k)
end = time.time()
print("Time Per Hash (s): " + str((end - start) / nElements))

# Save files for CLI testing
f_one = open('1column.txt', 'w')
f_two = open('2column.txt', 'w')

for k in keys:
    f_one.write(k + '\n')
    f_two.write(k + " " + k + '\n')

f_one.close()
f_two.close()

store = Store()

#
# Testing data structure and store object times
#

# Measure time to insert
avg_time = 0
for k in keys:
    start = time.time()
    store.put(k, k)
    end = time.time()
    avg_time += (end - start)
print("Time Per Allocaiton (s): " + str(avg_time / store.count))

# Measure time to read
avg_time = 0
for k in keys:
    start = time.time()
    tmp = store.get(k)
    end = time.time()
    avg_time += (end - start)
print("Time Per Read (s): " + str(avg_time / store.count))

# Measure time to remove
avg_time = 0
for k in keys:
    start = time.time()
    store.delete(k)
    end = time.time()
    avg_time += (end - start)
print("Time Per Delete (s): " + str(avg_time / len(keys)))

#
# Testing API service
#

print("Testing API service, persistent connection, no concurrency")
client = storeClient.StoreClient()
client.connect()

# Service/API Put time to test
avg_time = 0
times = []
for k in keys:
    start = time.time()
    client.put(k, k)
    end = time.time()
    avg_time += (end - start)
    times.append((end - start))
print("Time Per Insert API (s): " + str(avg_time / len(keys)))
df = pd.DataFrame(np.array(times))
print("90%, 95%, 99%: ", df[0].quantile(0.9), df[0].quantile(0.95), df[0].quantile(0.99))

# Service/API Get time to test
avg_time = 0
times = []
for k in keys:
    start = time.time()
    client.get(k)
    end = time.time()
    avg_time += (end - start)
    times.append((end - start))
print("Time Per Get API (s): " + str(avg_time / len(keys)))
df = pd.DataFrame(np.array(times))
print("90%, 95%, 99%: ", df[0].quantile(0.9), df[0].quantile(0.95), df[0].quantile(0.99))

# Service/API Delete time to test
avg_time = 0
times = []
for k in keys:
    start = time.time()
    client.delete(k)
    end = time.time()
    avg_time += (end - start)
    times.append((end - start))
print("Time Per Delete API (s): " + str(avg_time / len(keys)))
df = pd.DataFrame(np.array(times))
print("90%, 95%, 99%: ", df[0].quantile(0.9), df[0].quantile(0.95), df[0].quantile(0.99))
