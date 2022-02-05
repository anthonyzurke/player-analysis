# Player-Analysis

|Feature                         |Description                                |Dataset        |Type    |
|---                             |---                                        |---            |---     |
|pitch_type                      |Type of pitch from Statcast                |mlb-pitches  |object  |
|game_date                       |Date of the game                           |mlb-pitches  |object  |
|release_speed                   |out-of-hand pitch velocity                 |mlb-pitches  |float64 |
|release_pos_x                   |Horizontal Release Position of the ball measured in feet from the catcher's perspective |mlb-pitches | float64
|release_pos_z                   |Vertical Release Position of the ball measured in feet from the catcher's perspective | mlb-pitches | float64
|player_name                     |Player's name                              |mlb-pitches |object
|batter                          |MLB Player Id tied to the play event       |mlb-pitches |int64
|pitcher                         |MLB Player Id tied to the play event       |mlb-pitches |int64
|events                          |Event of the resulting Plate Appearance    |mlb-pitches |object
|description                     |Description of the resulting pitch         |mlb-pitches |object
|zone                            |Zone location of the ball when it crosses the plate from the catcher's perspective  |mlb-pitches | int64
|des                             |Plate appearance description from game day |mlb-pitches |object
|game_type                       |F = Wild Card, D = Divisional Series, L = League Championship Series, W = World Series |mlb-pitches | object
|stand                           |Side of the plate batter is standing       |mlb-pitches |object
|p_throws                        |Hand pitcher throws with                   |mlb-pitches |object
|home_team                       |Abbreviation of home team                  |mlb-pitches |object
|away_team                       |Abbreviation of away team                  |mlb-pitches |object
|type                            |Short hand of pitch result. B = ball, S = strike, X = in play  |mlb-pitches |object
|hit_location                    |Position of first fielder to touch the ball |mlb-pitches |float64
|bb_type                         |Batted ball type, ground_ball, line_drive, fly_ball, popup |mlb-pitches |object
|balls                           |Pre-pitch number of balls in count         |mlb-pitches |int64
|strikes                         |Pre-pitch number of strikes in count       |mlb-pitches |int64
|count                           |count of balls and strikes                 |mlb-pitches |object
|game_year                       |Year game took place 2021                  |mlb-pitches |int64
|pfx_x                           |Horizontal movement in feet from the catcher's perspective  |mlb-pitches |float64
|pfx_-x                  |Horizontal movement in feet from the pitchers's perspective  |mlb-pitches |float64
|pfx_z    |Vertical movement in feet from the catcher's perpsective  |mlb-pitches |float64
|plate_x  |Horizontal position of the ball when it crosses home plate from the catcher's perspective |mlb-pitches |float64
|plate_-x                        |Horizontal position of the ball when it crosses home plate from the pitcher's perspective  |mlb-pitches |float64
|plate_z  |Vertical position of the ball when it crosses home plate from the catcher's perspective   |mlb-pitches |float64
|on_3b                           |Pre-pitch MLB Player Id of Runner on 3B   |mlb-pitches |float64
|on_2b                           |Pre-pitch MLB Player Id of Runner on 2B   |float64
|on_1b                           |Pre-pitch MLB Player Id of Runner on 1B   |float64
|outs_when_up                    |Pre-pitch number of outs           |mlb-pitches |int64
|inning                          |Pre-pitch inning number           |mlb-pitches |int64
|inning_topbot                   |Pre-pitch top or bottom of inning         |mlb-pitches |object
|hc_x                            |Hit coordinate X of batted ball           |mlb-pitches |float64
|hc_y                            |Hit coordinate X of batted ball           |mlb-pitches |float64
|vx0                             |Pre-pitch MLB Player Id of Catcher     |mlb-pitches |float64
|vy0        |The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet  |mlb-pitches |float64
|vz0        |The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet  |mlb-pitches |float64
|ax        |The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet |mlb-pitches |float64
|ay        |The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet |mlb-pitches |float64
|az |The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet |mlb-pitches |float64
|sz_top  |Top of the batter's strike zone set by the operator when the ball is halfway to the plate  |mlb-pitches |float64
|sz_bot  |Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate |mlb-pitches |float64
|hit_distance_sc                 |Projected hit distance of the batted ball  |mlb-pitches |float64
|launch_speed                    |Exit velocity of the batted ball as tracked by Statcast  |mlb-pitches |float64
|launch_angle                    |Launch angle of the batted ball as tracked by Statcast  |mlb-pitches |float64
|effective_speed                 |Derived speed based on the the extension of the pitcher's release |mlb-pitches |float64
|release_spin_rate               |Spin rate of pitch tracked by Statcast    |mlb-pitches |float64
|release_extension               |Release extension of pitch in feet as tracked by Statcast  |mlb-pitches |float64
|game_pk                         |Unique Id for Game                   |mlb-pitches |int64
|release_pos_y   |Release position of pitch measured in feet from the catcher's perspective |mlb-pitches |float64
|estimated_ba_using_speedangle   |Estimated Batting Avg based on launch angle and exit velocity   |mlb-pitches |float64
|estimated_woba_using_speedangle |Estimated wOBA based on launch angle and exit velocity   |mlb-pitches |float64
|woba_value                      |wOBA value based on result of play           |mlb-pitches |float64
|woba_denom                      |wOBA denominator based on result of play  |mlb-pitches |float64
|babip_value                     |BABIP value based on result of play      |mlb-pitches |float64
|iso_value                       |ISO value based on result of play    |mlb-pitches |flaot64
|launch_speed_angle |Launch speed/angle 1: Weak 2: Topped 3: Under 4: Flare/Burner 5: Solid Contact 6: Barrel |mlb-pitches |float64
|at_bat_number        |Plate appearance number of the game           |mlb-pitches |int64
|pitch_number            |Total pitch number of the plate appearance    |mlb-pitches |int64
|pitch_name               |The name of the pitch derived from the Statcast Data  |mlb-pitches |object
|home_score               |Pre-pitch home score   |mlb-pitches |int64
|away_score           |Pre-pitch home score   |mlb-pitches |int64
|post_away_score        |Post-pitch home score     |mlb-pitches |int64
|post_home_score         |Post-pitch away score           |mlb-pitches | int64
|if_fielding_alignment   |Infield fielding alignment at the time of the pitch   |mlb-pitches |object
|of_fielding_alignment     |Outfield fielding alignment at the time of the pitch  |mlb-pitches |object
|spin_axis |The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball | mlb-pitches |float64
|delta_home_win_exp              |The change in Win Expectancy before the Plate Appearance and after the Plate Appearance |mlb-pitches | float64
|delta_run_exp                   |The change in Run Expectancy before the Pitch and after the Pitch |mlb-pitches |flaot64
|Mx |The amount of movement in the x-direction due to the Magnus effect alone. (Positive is towards first base/catcher's right) |mlb-pitches |float64
|Mz |The amount of movement in the z-direction due to the Magnus effect alone. (Positive is upwards) |mlb-pitches |float64
|theta                           |The angle of the spin axis with respect to it's movement between 0 and 90. A 0 angle means the spin axis is perpendicular to it's movement (it's all 'useful' spin with regards to the Magnus effect); 90 means the spin axis is parallel to it's direction (like a gyroball). Pitches |mlb-pitches |float64
|phi                             |The angle of the spin axis in the x-z plane oriented to the x-axis. More colloquially, the axis the ball is spinning from the catcher's eye. |mlb-pitches |float64
|bauer_units                   |spin rate / velocity |mlb-pitches |flaot64
|is_strike                   |if the result of the pitch is a strike 1 if not 0 |mlb-pitches |int64
|pitch_count                   |balls and strikes combined |mlb-pitches |object
|swing_miss                   |if the result of the pitch is a swing and miss 1 if not 0 |mlb-pitches |flaot64