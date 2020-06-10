# MSDS 453 Assignment 4
# Author: Ben Xiao

###### Setup #######
# Import packages
import sys
import pandas as pd
import numpy as np
import os
import re, string

# Check package versions
print('Check package version:')
print('Python: {}'.format(sys.version))
print('pandas: {}'.format(pd.__version__))
print('NumPy: {}'.format(np.__version__))
print('ReGex: {}'.format(re.__version__))

# Import and check data
data_path = 'data_files/filtered_games_data.json'
df = pd.read_json(data_path)

