import shape_calc
from unittest import main

#THIS IS THE FIRST DATA TESTED IN SHAPE_CALC.PY
rect = shape_calc.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calc.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

#THIS WILL RUN THE SHAPE_CALC_TEST AUTOMATICALLY
main(module='shape_calc_test', exit=False)
