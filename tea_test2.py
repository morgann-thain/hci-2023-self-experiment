import tea

data_path = "./simplified_data.csv"

variables = [
    {
        'name' : 'mood_score',
        'data type' : 'ratio'
    },
    {
        'name' : 'condition',
        'data type': 'nominal',
        'categories': ['A', 'B']
    },
    {
        'name' : 'ready_score',
        'data type' : 'ratio'
    }
]

study_design = {
    'study type': 'observational study',
    'contributor variables': 'condition',
    'outcome variables': 'mood_score'
}

assumptions = {
    'Type I (False Positive) Error Rate': 0.05,
}

tea.data(data_path, key="id")
tea.define_variables(variables)
tea.define_study_design(study_design)
tea.assume(assumptions)
tea.hypothesize(['condition', 'mood_score'], ['condition: A < B'])

'''
Results:
--------------
Test: kruskall_wallis
***Test assumptions:
Independent (not paired) observations: Plant
Exactly one explanatory variable: Plant
Exactly one explained variable: uptake
Continuous (not categorical) data: uptake
Variable is categorical: Plant
Variable has two or more categories: Plant

***Test results:
name = Kruskall Wallis
test_statistic = 6.89813
p_value = 0.22833
adjusted_p_value = 0.22833
alpha = 0.05
dof = 7
Null hypothesis = There is no difference in medians between Plant = Qn1, Qn2, Qn3, Qc1, Qc2, Qc3 on uptake.
Interpretation = t(7) = 6.89813, p = 0.22833. Fail to reject the null hypothesis at alpha = 0.05. There is no difference in medians between Plant = Qn1, Qn2, Qn3, Qc1, Qc2, Qc3 on uptake.
'''