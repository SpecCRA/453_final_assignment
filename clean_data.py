# MSDS 453 Assignment 4
# Author: Ben Xiao
# Cleaning and formatting data

# Setup

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

# Define important functions
def word_count(row):
    # Returns the number of words in a text review
    num_words = len(row)

    return num_words

# Import and check data
games_path = 'data_files/games_data.pkl'
games_df = pd.read_pickle(games_path)

#print(games_df.head())
# Check number of starting rows
start_len = len(games_df)
print('Starting number of rows: {}'.format(start_len))

# Check rows with no text review or no rating
empty_reviews = len(games_df[games_df.reviewText.isnull()])
empty_ratings = len(games_df[games_df.overall.isnull()])

print('Number of rows with empty reviews: {}'.format(empty_reviews))
print('Number of rows with empty ratings: {}'.format(empty_ratings))

games_df.dropna(how = 'any', inplace=True)

# Check statistics about number of words in reviews
games_df['word_counts'] = games_df['reviewText'].apply(word_count)

print('-------Word count descriptive statistics:--------\n')
print(games_df['word_counts'].describe())

# Remove reviews with less than 100 words
filtered_df = games_df[games_df.word_counts > 100]

filtered_row_count = len(filtered_df)
rows_removed = start_len - filtered_row_count
print('Number of removed rows: {}'.format(rows_removed))
print('Number of rows remaining: {}'.format(filtered_row_count))

print('------Filtered word count descriptive statistics------')
print(filtered_df.word_counts.describe())

# Pickle filtered data
filtered_df.to_json('data_files/filtered_games_data.json')

print('Script end.')