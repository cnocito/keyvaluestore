__author__ = 'cnocito'

import pandas as pd
import sys
import traceback
import math

if len(sys.argv) != 2:
    print("Invalid number of arguments!")
else:
    try:
        df = pd.DataFrame
        df= pd.read_csv(sys.argv[1],header=None,names=['time'])
        filename = sys.argv[1]
        mean = df['time'].values.mean()
        jitter = df['time'].values.std()
        count = df.count().values[0]
        p90 = df.quantile(0.90).values[0]
        p95 = df.quantile(0.95).values[0]
        p99 = df.quantile(0.99).values[0]
        print(filename,count,mean,jitter,p90,p95,p99)
    except:
        print(traceback.format_exc())
