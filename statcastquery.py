from pybaseball import playerid_lookup, statcast_pitcher, statcast_batter

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

playerid_lookup('chapman', 'aroldis')
chapman = statcast_pitcher('2021-04-01', '2021-10-04', 547973)
print(chapman.shape)
chapman.head()

chapman.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                      'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                      'umpire', 'sv_id'], inplace = True)

chapman['is_strike'] = [1 if x != 'B' else 0 for x in chapman['type']]
chapman['pitch_count'] = chapman[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

chapman['plate_-x'] = -chapman['plate_x']
chapman['pfx_-x'] = -chapman['pfx_x']
chapman['pfx_-x'] = 12 * chapman['pfx_-x']
chapman['pfx_z'] = 12 * chapman['pfx_z']

chapman['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
chapman['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
chapman['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in chapman['description']]

chapman.to_csv('./data/aroldis-chapman.csv')

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

playerid_lookup('hicks', 'jordan')

hicks = statcast_pitcher('2019-03-28', '2019-9-29', 663855)
print(hicks.shape)
hicks.head()

hicks.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                      'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                      'umpire', 'sv_id'], inplace = True)

hicks['is_strike'] = [1 if x != 'B' else 0 for x in hicks['type']]
hicks['pitch_count'] = hicks[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

hicks['plate_-x'] = -hicks['plate_x']
hicks['pfx_-x'] = -hicks['pfx_x']
hicks['pfx_-x'] = 12 * hicks['pfx_-x']
hicks['pfx_z'] = 12 * hicks['pfx_z']

hicks['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                             ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
hicks['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                         'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
hicks['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in hicks['description']]

hicks.to_csv('./data/jordan-hicks.csv')

playerid_lookup('lemahieu', 'dj')
lemahieu = statcast_batter('2021-04-01', '2021-10-04', 518934)
print(lemahieu.shape)
lemahieu.head()

lemahieu.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                         'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                         'umpire', 'sv_id'], inplace = True)

lemahieu['is_strike'] = [1 if x != 'B' else 0 for x in lemahieu['type']]
lemahieu['pitch_count'] = lemahieu[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

lemahieu['plate_-x'] = -lemahieu['plate_x']
lemahieu['pfx_-x'] = -lemahieu['pfx_x']
lemahieu['pfx_-x'] = 12 * lemahieu['pfx_-x']
lemahieu['pfx_z'] = 12 * lemahieu['pfx_z']

lemahieu['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                             ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
lemahieu['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                         'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
lemahieu['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in lemahieu['description']]

lemahieu.to_csv('./data/dj-lemahieu.csv')

playerid_lookup('stanton', 'giancarlo')
stanton = statcast_batter('2021-04-01', '2021-10-04', 519317)
print(stanton.shape)
stanton.head()

stanton.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                         'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                         'umpire', 'sv_id'], inplace = True)

stanton['is_strike'] = [1 if x != 'B' else 0 for x in stanton['type']]
stanton['pitch_count'] = stanton[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

stanton['plate_-x'] = -stanton['plate_x']
stanton['pfx_-x'] = -stanton['pfx_x']
stanton['pfx_-x'] = 12 * stanton['pfx_-x']
stanton['pfx_z'] = 12 * stanton['pfx_z']

stanton['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                             ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
stanton['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                         'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
stanton['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in stanton['description']]

stanton.to_csv('./data/giancarlo-stanton.csv')

playerid_lookup('judge', 'aaron')
judge = statcast_batter('2021-04-01', '2021-10-04', 592450)
print(judge.shape)
judge.head()

judge.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                         'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                         'umpire', 'sv_id'], inplace = True)

judge['is_strike'] = [1 if x != 'B' else 0 for x in judge['type']]
judge['pitch_count'] = judge[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

judge['plate_-x'] = -judge['plate_x']
judge['pfx_-x'] = -judge['pfx_x']
judge['pfx_-x'] = 12 * judge['pfx_-x']
judge['pfx_z'] = 12 * judge['pfx_z']

judge['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                             ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
judge['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                         'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
judge['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in judge['description']]

judge.to_csv('./data/aaron-judge.csv')