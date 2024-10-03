import sys
import os

# Add the parent directory of the current file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.features import *
from logic.formulas import *
from logic.rules import *


# Define features with their domains
color = Feature('color', {'red', 'green', 'blue'})

shape = Feature('shape', {'circle', 'square', 'rectangular'})

# Assignment of value to the feature
color_red = FeatureAtom(color, 'red')
shape_circle = FeatureAtom(shape, 'circle')

# Feature conjuntion
feature_formula = FeatureOr(color_red, shape_circle)
print(feature_formula)


# Define all possible class labels
class_labels = {'A', 'B', 'C'}

# Create classification formulas
class_A = ClassificationAtom('A')
class_B = ClassificationAtom('B')
class_C = ClassificationAtom('C')

# Classification formula: ¬B
classification_formula = ClassificationNot(class_B)

# Create a rule
rule = Rule(feature_formula, classification_formula)

# Print rule
print(rule)

# Get the head classes
head_classes = rule.head_classes(class_labels)
print(f"Head classes: {head_classes}")  # Output: Head classes: {'A', 'C'}
