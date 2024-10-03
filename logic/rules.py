from logic.formulas import *
from logic.features import *

class Rule(FeatureFormula):
    def __init__(self, body, head):
        """
        Represents a rule φ ⇒ ψ.
        :param body: A FeatureFormula instance.
        :param head: A ClassificationFormula instance.
        """
        if not isinstance(body, FeatureFormula):
            raise TypeError("Body must be a FeatureFormula")
        if not isinstance(head, ClassificationFormula):
            raise TypeError("Head must be a ClassificationFormula")
        self.body = body
        self.head = head

    def __repr__(self):
        return f"{self.body} ⇒ {self.head}"

    def evaluate(self, data_point, classification):
        """
        Evaluate the rule for a given data point and classification.
        :param data_point: A dictionary mapping feature names to values.
        :param classification: The class assigned to the data point.
        :return: True if the rule holds, False otherwise.
        """
        if self.body.evaluate(data_point):
            return self.head.evaluate(classification)
        else:
            return True  # The rule does not apply if the body is False

    def symbols(self):
        return self.body.symbols().union(self.head.symbols())

    def head_classes(self, class_labels):
        """
        Returns the set of class labels represented by the head.
        :param class_labels: Set of all possible class labels.
        """
        def extract_labels(formula):
            if isinstance(formula, ClassificationAtom):
                return {formula.label}
            elif isinstance(formula, ClassificationNot):
                return class_labels - extract_labels(formula.operand)
            elif isinstance(formula, ClassificationAnd):
                labels = class_labels
                for op in formula.operands:
                    labels = labels & extract_labels(op)
                return labels
            elif isinstance(formula, ClassificationOr):
                labels = set()
                for op in formula.operands:
                    labels = labels | extract_labels(op)
                return labels
            else:
                return set()

        return extract_labels(self.head)
