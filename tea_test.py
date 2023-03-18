import tea

data_path = "./filtered_data.csv"
tea.data(data_path, key="condition")

variables = [
    {
        'name' : 'condition',
        'data type' : 'nominal',
        'categories' : ['A', 'B']
    },
    {
        'name' : 'mood_score',
        'data type' : 'ratio'
        # 'range' : [1,5]
    },
    {
        'name' : 'ready_score',
        'data type' : 'ratio'
        # 'range' : [1,5]
    }
]
tea.define_variables(variables)

study_design = {
    'study type': 'experiment',
    'independent variables': 'condition',
    'dependent variables': ['mood_score', 'ready_score']
}
tea.define_study_design(study_design)


# assumptions = {
#     'Type I (False Positive) Error Rate': 0.05
# }
# tea.assume(assumptions) 

result1 = tea.hypothesize(['condition', 'mood_score'], ['condition: B > A']) 
result2 = tea.hypothesize(['condition', 'ready_score'], ['condition: B > A']) 

print("mood\n", result1)