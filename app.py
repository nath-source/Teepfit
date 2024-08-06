from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lose_fat')
def lose_fat():
    return render_template('lose-fat.html')

@app.route('/rock_hard_abs')
def rock_hard_abs():
    return render_template('rock-hard-abs.html')

@app.route('/six_pack_abs')
def six_pack_abs():
    return render_template('six-pack-abs.html')

# WORKOUT COMPLETED

@app.route('/workout_finished_lose_fat')
def workout_finished_lose_fat():
    return render_template('lose-fat-workout.html')

@app.route('/workout_finished_hard_abs')
def workout_finished_hard_abs():
    return render_template('rock-hard-workout.html')

@app.route('/workout_finished_six_pack')
def workout_finished_six_pack():
    return render_template('six-pack-workout.html')



# FITNESS PAGES

@app.route('/abdominal_crunches')
def abdominal_crunches():
    return render_template('abdominal-crunches.html')

@app.route('/abs_clockwise')
def abs_clockwise():
    return render_template('abs_clockwise.html')

@app.route('/abs_counterclockwise')
def abs_counterclockwise():
    return render_template('abs_counterclockwise.html')

@app.route('/bent_leg_twist')
def bent_leg_twist():
    return render_template('bent-leg-twist.html')

@app.route('/bicycle_crunches')
def bicycle_crunches():
    return render_template('bicycle-crunches.html')

@app.route('/clapping_crunches')
def clapping_crunches():
    return render_template('clapping-crunches.html')

@app.route('/cobra_stretch')
def cobra_stretch():
    return render_template('cobra-stretch.html')

@app.route('/cobras')
def cobras():
    return render_template('cobras.html')

@app.route('/cross_arm_crunches')
def cross_arm_crunches():
    return render_template('cross-arm-crunches.html')

@app.route('/crunch_kicks')
def crunch_kicks():
    return render_template('crunch_kicks.html')

@app.route('/flutter_kicks')
def flutter_kicks():
    return render_template('flutter-kicks.html')

@app.route('/heel_touch')
def heel_touch():
    return render_template('heel_touch.html')

@app.route('/heels_to_the_heaven')
def heels_to_the_heaven():
    return render_template('heels-to-the-heaven.html')

@app.route('/high_stepping')
def high_stepping():
    return render_template('high-stepping.html')

@app.route('/jacks')
def jacks():
    return render_template('jacks.html')

@app.route('/leg_raises')
def leg_raises():
    return render_template('leg-raises.html')

@app.route('/long_arm_crunch')
def long_arm_crunch():
    return render_template('long_arm_crunch.html')

@app.route('/lying_swing_left')
def lying_swing_left():
    return render_template('lying-swing-left.html')

@app.route('/lying_swing_right')
def lying_swing_right():
    return render_template('lying-swing-right.html')

@app.route('/oblique_twist')
def oblique_twist():
    return render_template('oblique-twist.html')

@app.route('/plank')
def plank():
    return render_template('plank.html')

@app.route('/reverse_crunches_leg_raised')
def reverse_crunches_leg_raised():
    return render_template('reverse-crunches-leg-raised.html')

@app.route('/reverse_crunches')
def reverse_crunches():
    return render_template('reverse-crunches.html')

@app.route('/russian_twist')
def russian_twist():
    return render_template('russian-twist.html')

@app.route('/side_leg_raise_left')
def side_leg_raise_left():
    return render_template('side-leg-raise-left.html')

@app.route('/side_leg_raise_right')
def side_leg_raise_right():
    return render_template('side-leg-raise-right.html')

@app.route('/sit_up_twist')
def sit_up_twist():
    return render_template('sit-up-twist.html')

@app.route('/sit_ups')
def sit_ups():
    return render_template('sit-ups.html')

@app.route('/slow_mountain_climber')
def slow_mountain_climber():
    return render_template('slow-mountain-climber.html')

@app.route('/standing_bicycle_crunches')
def standing_bicycle_crunches():
    return render_template('standing-bicycle-crunches.html')

@app.route('/superman')
def superman():
    return render_template('superman.html')

@app.route('/swimmer_and_superman')
def swimmer_and_superman():
    return render_template('swimmer-and-superman.html')

@app.route('/t_plank_left')
def t_plank_left():
    return render_template('t-plank-left.html')

@app.route('/t_plank_right')
def t_plank_right():
    return render_template('t-plank-right.html')

@app.route('/v_up')
def v_up():
    return render_template('v-up.html')

if __name__ == '__main__':
    app.run(debug=True)
