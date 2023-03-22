import pandas as pd
data= pd.read_csv("filtered_data_dropped.csv")

# Drop rows with missing data for either mood_score or ready_score
data.dropna(subset=['mood_score', 'ready_score'], inplace=True)
data.to_csv("filtered_data_dropped.csv", index=False)

condition_a_data = data.loc[data['condition'] == 'A', ['mood_score', 'ready_score']]
condition_b_data = data.loc[data['condition'] == 'B', ['mood_score', 'ready_score']]

from scipy.stats import ttest_rel
t_statistic, p_value = ttest_rel(condition_a_data, condition_b_data)

print("t-statistic:", t_statistic)
print("p-value:", p_value)

# ChatGPT: f you want to do a t-test, the best option would be a paired t-test. A paired t-test is appropriate when you have two samples that are not independent, but instead are "paired" or "matched" in some way, such as when you have the same person measured under two different conditions (e.g., before and after an intervention) or in your case, the same person on two different days (meditating or not meditating).

# Although a paired t-test assumes that the differences between the two groups are normally distributed, it can still provide reasonable results even if this assumption is not met, especially if the sample size is large enough. Therefore, a paired t-test would be a good option for your analysis.