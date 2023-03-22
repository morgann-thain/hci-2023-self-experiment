# hci-2023-self-experiment

## activate the venv
`source venv/bin/activate`

## EXPERIMENT
Goal: LEARN if Journal+Meditation IMPROVES mood/productivity, worth the time/habit/boredom

Day-randomized A/B Testing: Google Flip a Coin each Day for Each Interval/Work Period: Heads do / Tails don’t. Do 3 times a day and/or before each work period

Confounding factors: weather, caffeine, day, etc.

## HYPOTHESIS
Hypothesis: 2-5 of Journalling immediate thoughts, todos, worries, feelings followed by 2-5min of breath or body mindfulness meditation will increase average mood by 1 point and average readiness by 1 hour.

## RESULTS
`pandas_independent_t_test.csv`:
- t-statistic: [-2.23995112 -1.3190019 ]
- p-value: 
	- mood_score: 0.04066496 
	- ready_score: 0.20695095]
- p < .05 for both => journaling + meditation has a statistically significant effect on mood and readiness

`cohens_d.py`
- d_mood:  -1.1038599655158243
- d_ready:  -0.6500112348102788

## COHEN'S D QUICK TABLE
Small Effect Size: d=0.20
Medium Effect Size: d=0.50
Large Effect Size: d=0.80

## DATA DEFINITIONS
Mood (mood_score = avg of the three):
- Happy: (pleasure contentness satisfaction)
- Calm: (NOT overstimulation/stress/hyperactivity/restlessness)
- Focus: (flow, presentness, productivity feelings NOT stray thoughts)

Readiness (ready_score = avg of the three):  
- Break: (how many hours i could work straight / before i need a break)
- Worked: (how many hours I have worked)
- Rest of Day: (How many hours of productivity left in the day…Energy > motivation?)
