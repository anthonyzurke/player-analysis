both = {}
right_handed = {}
left_handed = {}

pitch = ['SL', 'FF', 'CU', 'CH']

for type in order:
    # all hitters
    both[type] = kershaw.loc[kershaw['pitch_type'] == type]
    # RHH
    right_handed[type] = kershaw.loc[kershaw['stand'] == 'R' & kershaw['pitch_type'] == type]
    # LHH
    left_handed[type] = kershaw.loc[kershaw['stand'] == 'L' & kershaw['pitch_type'] == type]