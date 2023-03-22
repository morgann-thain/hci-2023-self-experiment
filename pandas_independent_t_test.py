import pandas as pd
from scipy.stats import ttest_ind

# Load the data
data = pd.read_csv("filtered_data.csv")

# Split the data into two groups
mood_A = data.loc[data['condition'] == 'A', 'mood_score']
mood_B = data.loc[data['condition'] == 'B', 'mood_score']

print(mood_A)

ready_A = data.loc[data['condition'] == 'A', 'ready_score']
ready_B = data.loc[data['condition'] == 'B', 'ready_score']


# Perform the t-test
mood_t, mood_p = ttest_ind(a=mood_A,b=mood_B,equal_var=True)
ready_t, ready_p = ttest_ind(a=ready_A,b=ready_B,equal_var=True)


# Print the results
print("Mood")
print("t-statistic:", mood_t)
print("p-value:", mood_p)

print("\nReady")
print("t-statistic:", ready_t)
print("p-value:", ready_p)
