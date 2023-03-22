import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


# Load your data into a pandas DataFrame
data = pd.read_csv('filtered_data_m.csv')

data['condition'] = data['condition'].astype('category')

# Convert the date column to a datetime object
data['date'] = pd.to_datetime(data['date'])

# Create a new column for the hour of the day
data['hour'] = data['time'].str.split(':').str[0].astype(int)

# Create a new column for the time of day
data['time_of_day'] = pd.cut(data['hour'], bins=[0, 12, 18, 24], labels=['morning', 'afternoon', 'evening'], include_lowest=True)

print(data)

# Use time_of_day and condition as the within-subject factors
model = ols('mood_score ~ C(time_of_day) + C(condition) + C(time_of_day):C(condition)', data=data).fit()

# Use ANOVA to test for significant effects
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
