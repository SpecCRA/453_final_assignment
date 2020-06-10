import pandas as pd
import numpy as np
import json
import sys
import os

print('Python: {}'.format(sys.version))
print('pandas: {}'.format(pd.__version__))
print('NumPy: {}'.format(np.__version__))

games_path = 'data_files/Video_Games.json'

data = list()

with open(games_path) as f:
    for line in f:
        data.append(json.loads(line.strip()))

games_df = pd.DataFrame(data)
# Retain rating, text review, and ID of product
export_df = games_df[['overall', 'reviewText', 'asin']]

print('Rows exported: {}'.format(len(export_df)))

print('pickling started')
export_df.to_pickle('games_data.pkl')
print('pickling done')