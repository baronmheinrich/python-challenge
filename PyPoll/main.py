import os
import pandas as pd

# Define the file_path and dataframe
df1_path = os.path.join('raw_data', 'election_data_1.csv')
voter_df1 = pd.read_csv(df1_path)

candidates = voter_df1['Candidate'].unique()
total_votes = len(voter_df1.index) - 1

cand_groups = voter_df1.groupby(['Candidate'])
vote_counts = cand_groups['Voter ID'].count()
vote_counts = vote_counts.to_frame()
vote_counts = vote_counts.rename(columns={'Voter ID': 'Total Votes'})

candidate_list = voter_df1['Candidate'].value_counts().keys().tolist()
vote_counts = voter_df1['Candidate'].value_counts().tolist()
winning_number = voter_df1['Candidate'].value_counts().max()
vote_per_cand = list(zip(candidates, vote_counts))

for i in range(len(vote_per_cand) - 1):
    if vote_per_cand[i][1] == winning_number:
        winner = vote_per_cand[i][0]

print('Election Results')
print('---------------------------')
print('Total votes: {}'.format(total_votes))
print('---------------------------')

for candidate in candidates:
    vote_count = vote_counts.at[candidate, 'Total Votes']
    vote_percentage = round((vote_count / total_votes) * 100, 2)
    print('{}: {}% ({})'.format(candidate, vote_percentage, vote_count))

print('Winner: {}'.format(winner))
