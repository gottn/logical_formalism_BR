from logic.formulas import *
class Feature:
    def __init__(self, name, domain) -> None:
        """
        Initialize a feature with a name and a domain of possible values.
        :param name: Name of the feature
        :param domain: A set of possible values for the feature (finite and discrete for now)
        """
        self.name = name
        self.domain = domain

    def __repr__(self) -> str:
        return f"Feature({self.name})"
    
    def __eq__(self, other):
        return isinstance(other, Feature) and self.name == other.name
    
    def __hash__(self) -> int:
        return hash(('feature', self.name))
    
class FeatureAtom(FeatureFormula):
    def __init__(self, feature, value) -> None:
        """
        Represents a feature atom (f, v)
        :param feature: An instance of Feature
        :param value: A value from feature.domain
        """
        if value not in feature.domain:
            raise ValueError(f"Value {value} not in domain of feature {feature.name}")
        self.feature = feature
        self.value = value

    def __repr__(self) -> str:
        return f"({self.feature.name}, {self.value})"
    
    def evaluate(self, data_point):
        """
        Evaluate the atom against a data point.
        :param data_point: A dictionary mapping feature names to values.
        :return: True if the data point assings the specified value to the feature
        """

        return data_point.get(self.feature.name) == self.value
    
    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FeatureAtom) and 
            self.feature == other.feature and
            self.value == other.value
        )
    
    def __hash__(self) -> int:
        return hash(('feature_atom', self.feature, self.value))
    


class ClassificationAtom(ClassificationFormula):
    def __init__(self, label):
        """
        Represents a classification atom (class label).
        :param label: A string representing the class label
        """
        self.label = label

    def __repr__(self) -> str:
        return f"{self.label}"
    
    def evaluate(self, classification):
        """
        Evaluate the atom against a classificaiton.
        :param classification: The class assigned to a data point.
        :return: True if the classification matches the atom's label.
        """
        return self.label == classification
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, ClassificationAtom) and self.label == other.label
    
    def __hash__(self) -> int:
        return hash(('classification_atom', self.label))



    

 
        