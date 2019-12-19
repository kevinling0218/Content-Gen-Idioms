'''This module convert the csv file crawled from web into a txt file for training'''
import pandas as pd

df = pd.read_csv('idioms - theIdioms.csv')
df['uses'].to_csv('idioms_uses.txt', index = False, header=False)