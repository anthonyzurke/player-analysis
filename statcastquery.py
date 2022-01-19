#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pybaseball import playerid_lookup, statcast_pitcher

playerid_lookup('cole', 'gerrit')

cole = statcast_pitcher('2021-04-01', '2021-10-04', 543037)
print(cole.shape)

cole.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                     'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                     'umpire', 'sv_id'], inplace = True)
# Create is_strike column
cole['is_strike'] = [1 if x != 'B' else 0 for x in cole['type']]
# Create pitch_count column
cole['pitch_count'] = cole[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

# Switch from catcher's perspective to pitcher's perspective
# Catcher's POV: (plate_x, plate_z)
# Pitcher's POV: (plate_-x, plate_z)
cole['plate_-x'] = -cole['plate_x']
# Switch HB to perspective of pitcher
# Catcher's POV: (pfx_x, pfx_z)
# Pitcher's POV: (pfx_-x, pfx_z)
cole['pfx_-x'] = -cole['pfx_x']
# HB and VB in feet should be in inches (*12)
#cole['pfx_x'] = 12 * cole['pfx_x']
cole['pfx_-x'] = 12 * cole['pfx_-x']
cole['pfx_z'] = 12 * cole['pfx_z']

# Replace values
cole['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
# Make all events that aren't hits, outs
cole['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
# make swing_miss column
cole['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in cole['description']]

cole.to_csv('./data/gerrit-cole.csv')

playerid_lookup('wainwright', 'adam')

wain = statcast_pitcher('2021-04-01', '2021-10-04', 425794)
print(wain.shape)
wain.head()

wain.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                     'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                     'umpire', 'sv_id'], inplace = True)

wain['is_strike'] = [1 if x != 'B' else 0 for x in wain['type']]
wain['pitch_count'] = wain[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

wain['plate_-x'] = -wain['plate_x']
wain['pfx_-x'] = -wain['pfx_x']
wain['pfx_-x'] = 12 * wain['pfx_-x']
wain['pfx_z'] = 12 * wain['pfx_z']

wain['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
wain['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
wain['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in wain['description']]

wain.to_csv('./data/adam-wainwright.csv')

playerid_lookup('nola', 'aaron')

nola = statcast_pitcher('2021-04-01', '2021-10-04', 605400)
print(nola.shape)
nola.head()

nola.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                     'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                     'umpire', 'sv_id'], inplace = True)

nola['is_strike'] = [1 if x != 'B' else 0 for x in nola['type']]
nola['pitch_count'] = nola[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

nola['plate_-x'] = -nola['plate_x']
nola['pfx_-x'] = -nola['pfx_x']
nola['pfx_-x'] = 12 * nola['pfx_-x']
nola['pfx_z'] = 12 * nola['pfx_z']

nola['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
nola['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
nola['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in nola['description']]

nola.to_csv('./data/arron-nola.csv')

playerid_lookup('fried', 'max')

fried = statcast_pitcher('2021-04-01', '2021-10-04', 608331)
print(fried.shape)
fried.head()

fried.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                      'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                      'umpire', 'sv_id'], inplace = True)

fried['is_strike'] = [1 if x != 'B' else 0 for x in fried['type']]
fried['pitch_count'] = fried[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

fried['plate_-x'] = -fried['plate_x']
fried['pfx_-x'] = -fried['pfx_x']
fried['pfx_-x'] = 12 * fried['pfx_-x']
fried['pfx_z'] = 12 * fried['pfx_z']

fried['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
fried['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
fried['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in fried['description']]

fried.to_csv('./data/max-fried.csv')

