# Player-Analysis
---

## Data Collection

I used the pybaseball package to receive statcast hitting and pitching/spin data from Baseball Savant

## Data Dictionary
|Feature                         |Description                                |Dataset        |Type    |
|---                             |---                                        |---            |---     |
|pitch_type                      |Type of pitch from Statcast                |hitters / pitchers  |object  |
|game_date                       |Date of the game                           |hitters / pitchers  |object  |
|release_speed                   |Out-of-hand pitch velocity                 |hitters / pitchers  |float64 |
|release_pos_x       |Horizontal Release Position of the ball measured in feet from the catcher's perspective |hitters / pitchers | float64 |
|release_pos_z |Vertical Release Position of the ball measured in feet from the catcher's perspective | hitters / pitchers | float64 |
|player_name                     |Player's name                              |hitters / pitchers |object
|batter                          |MLB Player Id tied to the play event       |hitters / pitchers |int64
|pitcher                         |MLB Player Id tied to the play event       |hitters / pitchers |int64
|events                          |Event of the resulting Plate Appearance    |hitters / pitchers |object
|description                     |Description of the resulting pitch         |hitters / pitchers |object
|zone                            |Zone location of the ball when it crosses the plate from the catcher's perspective  |hitters / pitchers | int64
|des                             |Plate appearance description from game day |hitters / pitchers |object
|stand                           |Side of the plate batter is standing       |hitters / pitchers |object
|p_throws                        |Hand pitcher throws with                   |hitters / pitchers |object
|home_team                       |Abbreviation of home team                  |hitters / pitchers |object
|away_team                       |Abbreviation of away team                  |hitters / pitchers |object
|type                            |Short hand of pitch result. B = ball, S = strike, X = in play  |hitters / pitchers |object
|hit_location                    |Position of first fielder to touch the ball |hitters / pitchers |float64
|bb_type                         |Batted ball type, ground_ball, line_drive, fly_ball, popup |hitters / pitchers |object
|balls                           |Pre-pitch number of balls in count         |hitters / pitchers |int64
|strikes                         |Pre-pitch number of strikes in count       |hitters / pitchers |int64
|count                           |count of balls and strikes                 |hitters / pitchers |object
|game_year                       |Year game took place 2021                  |hitters / pitchers |int64
|pfx_x                           |Horizontal movement in feet from the catcher's perspective  |hitters / pitchers |float64
|pfx_-x                  |Horizontal movement in feet from the pitchers's perspective  |hitters / pitchers |float64
|pfx_z    |Vertical movement in feet from the catcher's perpsective  |hitters / pitchers |float64
|plate_x  |Horizontal position of the ball when it crosses home plate from the catcher's perspective |hitters / pitchers |float64
|plate_-x                        |Horizontal position of the ball when it crosses home plate from the pitcher's perspective  |hitters / pitchers |float64
|plate_z  |Vertical position of the ball when it crosses home plate from the catcher's perspective   |hitters / pitchers |float64
|on_3b                           |Pre-pitch MLB Player Id of Runner on 3B   |hitters / pitchers |float64
|on_2b                           |Pre-pitch MLB Player Id of Runner on 2B   |float64
|on_1b                           |Pre-pitch MLB Player Id of Runner on 1B   |float64
|outs_when_up                    |Pre-pitch number of outs           |hitters / pitchers |int64
|inning                          |Pre-pitch inning number           |hitters / pitchers |int64
|inning_topbot                   |Pre-pitch top or bottom of inning         |hitters / pitchers |object
|hc_x                            |Hit coordinate X of batted ball           |hitters / pitchers |float64
|hc_y                            |Hit coordinate X of batted ball           |hitters / pitchers |float64
|vx0                             |Pre-pitch MLB Player Id of Catcher     |hitters / pitchers |float64
|vy0        |The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet  |hitters / pitchers |float64
|vz0        |The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet  |hitters / pitchers |float64
|ax        |The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet |hitters / pitchers |float64
|ay        |The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet |hitters / pitchers |float64
|az |The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet |hitters / pitchers |float64
|sz_top  |Top of the batter's strike zone set by the operator when the ball is halfway to the plate  |hitters / pitchers |float64
|sz_bot  |Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate |hitters / pitchers |float64
|hit_distance_sc                 |Projected hit distance of the batted ball  |hitters / pitchers |float64
|launch_speed                    |Exit velocity of the batted ball as tracked by Statcast  |hitters / pitchers |float64
|launch_angle                    |Launch angle of the batted ball as tracked by Statcast  |hitters / pitchers |float64
|effective_speed                 |Derived speed based on the the extension of the pitcher's release |hitters / pitchers |float64
|release_spin_rate               |Spin rate of pitch tracked by Statcast    |hitters / pitchers |float64
|release_extension               |Release extension of pitch in feet as tracked by Statcast  |hitters / pitchers |float64
|game_pk                         |Unique Id for Game                   |hitters / pitchers |int64
|release_pos_y   |Release position of pitch measured in feet from the catcher's perspective |hitters / pitchers |float64
|estimated_ba_using_speedangle   |Estimated Batting Avg based on launch angle and exit velocity   |hitters / pitchers |float64
|estimated_woba_using_speedangle |Estimated wOBA based on launch angle and exit velocity   |hitters / pitchers |float64
|woba_value                      |wOBA value based on result of play           |hitters / pitchers |float64
|woba_denom                      |wOBA denominator based on result of play  |hitters / pitchers |float64
|babip_value                     |BABIP value based on result of play      |hitters / pitchers |float64
|iso_value                       |ISO value based on result of play    |hitters / pitchers |flaot64
|launch_speed_angle |Launch speed/angle 1: Weak 2: Topped 3: Under 4: Flare/Burner 5: Solid Contact 6: Barrel |hitters / pitchers |float64
|at_bat_number        |Plate appearance number of the game           |hitters / pitchers |int64
|pitch_number            |Total pitch number of the plate appearance    |hitters / pitchers |int64
|pitch_name               |The name of the pitch derived from the Statcast Data  |hitters / pitchers |object
|home_score               |Pre-pitch home score   |hitters / pitchers |int64
|away_score         Pre-pitch home score   |hitters / pitchers |int64
|post_away_score     |Post-pitch home score     |hitters / pitchers |int64
|post_home_score     |Post-pitch away score           |hitters / pitchers | int64
|if_fielding_alignment |Infield fielding alignment at the time of the pitch   |hitters / pitchers |object
|of_fielding_alignment |Outfield fielding alignment at the time of the pitch  |hitters / pitchers |object
|spin_axis |The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball | hitters / pitchers |float64
|delta_home_win_exp |The change in Win Expectancy before the Plate Appearance and after the Plate Appearance |hitters / pitchers | float64
|delta_run_exp  |The change in Run Expectancy before the Pitch and after the Pitch |hitters / pitchers |flaot64
|Mx |The amount of movement in the x-direction due to the Magnus effect alone. (Positive is towards first base/catcher's right) |hitters / pitchers |float64
|Mz |The amount of movement in the z-direction due to the Magnus effect alone. (Positive is upwards) |hitters / pitchers |float64
|theta |The angle of the spin axis with respect to it's movement between 0 and 90. A 0 angle means the spin axis is perpendicular to it's movement (it's all 'useful' spin with regards to the Magnus effect); 90 means the spin axis is parallel to it's direction (like a gyroball).|hitters / pitchers |float64
|phi |The angle of the spin axis in the x-z plane oriented to the x-axis. More colloquially, the axis the ball is spinning from the catcher's eye. |hitters / pitchers |float64
|bauer_units  |Spin Rate / Velocity |hitters / pitchers |flaot64
|is_strike  |1: If the result of the pitch is a strike 0: if not |hitters / pitchers |int64
|pitch_count   |Balls and strikes combined |hitters / pitchers |object
|swing_miss   |1: If the result of the pitch is a swing and miss 0: if not |hitters / pitchers |flaot64
|first_pitch_take |1: If hitter took the first pitch 0: if hitter didn't take first pitch |hitters |float64
|first_pitch_swing |1: If hitter swung at first pitch 0: if hitter took first pitch| hitters | float64
|in_zone_take | 1: if hitter took a pitch in the zone 0: if hitter swung at strike/took ball| hitters | float64
|out_of_zone_chase |1: If hitter chased out of the zone 0: if hitter took pitch out of the zone |hitters | float64