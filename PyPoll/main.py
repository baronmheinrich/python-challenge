import os
import pandas as pd

df1_path = os.path.join('raw_data', 'election_data_1.csv')
df2_path = os.path.join('raw_data', 'election_data_2.csv')

voter_df1 = pd.read_csv(df1_path)
voter_df2 = pd.read_csv(df2_path)

candidates = voter_df1['Candidate'].unique()
total_votes = len(voter_df1.index) - 1

cand_groups = voter_df1.groupby(['Candidate'])
vote_counts = cand_groups['Voter ID'].count()
vote_counts = vote_counts.to_frame()
vote_counts = vote_counts.rename(columns={'Voter ID': 'Total Votes'})

print('Election Results')
print('---------------------------')
print('Total votes: {}'.format(total_votes))
print('---------------------------')

for candidate in candidates:
    vote_count = vote_counts.at[candidate, 'Total Votes']
    vote_percentage = round((vote_count / total_votes) * 100, 2)
    print('{}: {}% ({})'.format(candidate, vote_percentage, vote_count))


