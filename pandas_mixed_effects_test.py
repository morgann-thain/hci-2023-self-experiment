import pandas as pd
import statsmodels.formula.api as smf

# Load data into a pandas dataframe
df = pd.read_csv("filtered_data.csv")

df['date'] = pd.to_datetime(df['date'])

# Create a new column for the hour of the day
df['hour'] = df['time'].str.split(':').str[0].astype(int)

# Create a new column for the time of day
df['time_of_day'] = pd.cut(df['hour'], bins=[0, 12, 18, 24], labels=['morning', 'afternoon', 'evening'], include_lowest=True)

# Convert date to integer days since a reference date
ref_date = pd.to_datetime('1970-01-01')
df['date'] = (df['date'] - ref_date).dt.days.astype(int)

# Create a new column with categorical values for meditation
df["meditation"] = pd.Categorical(df["condition"], categories=["A", "B"], ordered=False)

# Drop the original condition column
# df.drop("condition", axis=1, inplace=True)

# Define the model formula with the independent variable and random effect
mood_formula = "mood_score ~ C(condition)"
ready_formula = "ready_score ~ C(condition)"


# model_formula = "mood_score ~ condition + time_of_day + (1|date)"

# A grouping variable, on the other hand, is a variable that is used to group the data into subsets based on some characteristic that is not of primary interest in the analysis, but which may affect the relationship between the independent and dependent variables. Grouping variables are typically included as random effects in a mixed-effects model, which allows for the estimation of the between-group variance and the within-group variance separately.

#  random effects. This would allow you to capture the variation in mood scores across different dates and times of day, without explicitly modeling their effects on mood scores.

# Fit the linear mixed-effects model
mood_model = smf.mixedlm(mood_formula, df, groups=df["time_of_day"], exog_re=df['date']).fit(maxiter=10000, tol=1e-6, optimizer='adam')
ready_model = smf.mixedlm(ready_formula, df, groups=df["time_of_day"], exog_re=df['date']).fit(maxiter=10000, tol=1e-6, optimizer='adam')

# Print the model summary to see the results
print(mood_model.summary())
print(ready_model.summary())



# =========================================================
# Model:             MixedLM Dependent Variable: mood_score
# No. Observations:  17      Method:             REML      
# No. Groups:        3       Scale:              0.1465    
# Min. group size:   1       Log-Likelihood:     -9.9991   
# Max. group size:   8       Converged:          Yes       
# Mean group size:   5.7                                   
# ---------------------------------------------------------
#                 Coef. Std.Err.   z    P>|z| [0.025 0.975]
# ---------------------------------------------------------
# Intercept       3.038    0.201 15.144 0.000  2.645  3.431
# meditation[T.B] 0.543    0.193  2.820 0.005  0.166  0.920
# Group Var       0.066    0.254                           
# =========================================================


# Sure! Here's what the output means:

# The intercept term is 3.038. This represents the expected value of the mood score when all other variables in the model (i.e., meditation) are set to zero.
# The coefficient for the meditation variable (specifically, the level "B") is 0.543. This means that when the meditation level is B (compared to level A, which is the reference level), the mood score is expected to be higher by 0.543 units, all other variables being equal.
# The "Group Var" row shows the estimate of the variance of the random intercepts for each group. In this case, since there are three groups (one for each day), this represents the variability in the intercepts across the three days. The estimated variance is 0.066, which indicates that there is some variation in the mood scores across days that is not explained by the other variables in the model.
# In terms of statistical significance, both the intercept and meditation level B coefficient have p-values less than 0.05, which means they are statistically significant at the 0.05 level. This suggests that both variables are important in predicting mood scores.