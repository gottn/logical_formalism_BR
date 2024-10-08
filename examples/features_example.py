import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.features import *
from logic.formulas import *


# Define features with their domains
color = Feature('color', {'red', 'green', 'blue'})

shape = Feature('shape', {'circle', 'square', 'rectangular'})

# Assignment of value to the feature
color_red = FeatureAtom(color, 'red')
shape_circle = FeatureAtom(shape, 'circle')

# Feature conjuntion
feature_formula = FeatureOr(color_red, shape_circle)
print(feature_formula)


# Evaluating the formula
data_point = {'color': 'red', 'shape': 'circle'}



print(feature_formula.evaluate(data_point))  # Output: True
