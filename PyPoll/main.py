import pandas as pd

voter_df1 = pd.read_csv('raw_data/election_data_1.csv')
voter_df2 = pd.read_csv('raw_data/election_data_2.csv')

total_votes = len(voter_df1.index) - 1
candidates = df['Candidate'].unique()
print("{}: {}%".format())
