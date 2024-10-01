import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.features import *


# Define features with their domains
color = Feature('color', {'red', 'green', 'blue'})

# Assignment of value to the feature
color_red = FeatureAtom(color, 'red')

class_A = ClassificationAtom('A')

print(color_red)

print(class_A)