import os
import csv

path = os.path.join('raw_data', 'election_data_1.csv')

with open(path, 'r') as csvfile:
    reader = csv.reader(path)
 	
 	candiates = []
 	vote_counts = []

 	print(reader[0][1])