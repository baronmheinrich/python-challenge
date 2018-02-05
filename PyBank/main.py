import os
import pandas as pd

# Load test data
bank_csv_path = os.path.join('raw_data', 'budget_data_1.csv')
bank_df = pd.read_csv(bank_csv_path)

total_months = len(bank_df['Date'].unique())
total_revenue = bank_df['Revenue'].sum()

revenue_deltas = []

for i in range(len(bank_df['Revenue']) - 1):
    revenue_deltas.append(bank_df.loc[i + 1, 'Revenue'] - bank_df.loc[i, 'Revenue'])

avg_delta = sum(abs(delta) for delta in revenue_deltas) / len(revenue_deltas)

greatest_increase = 0
prev_increase = 0
date_increase = ''

for i in range(len(bank_df['Revenue']) - 1):
    curr_cell = bank_df.loc[i, 'Revenue']
    next_cell = bank_df.loc[i + 1, 'Revenue']

    if next_cell > curr_cell:
        increase = next_cell - curr_cell
        if increase > prev_increase:
            greatest_increase = increase
            date_increase = bank_df.loc[i, 'Date']
        else:
            increase = prev_increase
    else:
        continue

greatest_decrease = 0
prev_decrease = 0
date_decrease = ''

for i in range(len(bank_df['Revenue']) - 1):
    curr_cell = bank_df.loc[i, 'Revenue']
    next_cell = bank_df.loc[i + 1, 'Revenue']

    if next_cell < curr_cell:
        decrease = curr_cell - next_cell
        if decrease > prev_decrease:
            greatest_decrease = decrease
            date_decrease = bank_df.loc[i, 'Date']
        else:
            prev_decrease = decrease
    else:
        continue

print('\nFinancial Analysis')
print('----------------------------')
print('Total Months: {}'.format(total_months))
print('Total Revenue: ${}'. format(total_revenue))
print('Average Revenue Change: ${}'.format(avg_delta))
print('Greatest Increase in Revenue: {} ${}'.format(date_increase, greatest_increase))
print('Greatest Decrease in Revenue: {} $-{}\n'.format(date_decrease, greatest_decrease))
