# SOURCES
# 
# https://machinelearningmastery.com/effect-size-measures-in-python/
from numpy import std, mean, sqrt
import pandas as pd

#correct if the population S.D. is expected to be equal for the two groups.
def cohen_d(x,y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)

# data
df = pd.read_csv('filtered_data.csv')

A = df.loc[df['condition'] == 'A']
B = df.loc[df['condition'] == 'B']


mood_score_A = A['mood_score']
mood_score_B = B['mood_score']

ready_score_A = A['ready_score']
ready_score_B = B['ready_score']


#correct only if nx=ny
d_mood = cohen_d(mood_score_A,mood_score_B)
d_ready = cohen_d(ready_score_A,ready_score_B)

print('d_mood: ', d_mood)
print('d_ready: ', d_ready)

# Small Effect Size: d=0.20
# Medium Effect Size: d=0.50
# Large Effect Size: d=0.80

