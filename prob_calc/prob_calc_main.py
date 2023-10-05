# THIS IS THE MAIN FILE RUN TO TEST THE PROB_CALC PROGRAM.

import prob_calc
from unittest import main

hat = prob_calc.Hat(blue=4, red=2, green=6)
probability = prob_calc.experiment(
    hat = hat,
    expected_balls = {"blue": 2, "red": 1},
    num_balls_drawn = 4,
    num_experiments = 3000)
print("Probability:", probability)

# Run PROB_CALC_TEST automatically
#main(module='prob_calc_test', exit=False)
