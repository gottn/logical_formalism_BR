class Formula:
    def evaluate(self, context):
        """
        Evaluate the formula given a context.
        :param context: A dictionary or value for evaluation
        :return: Boolean value
        """
        raise NotImplementedError
    
    def symbols(self):
        """
        Return the set of symbols in the formula
        """
        raise NotImplementedError
    
    def __and__(self, other):
        return And(self, other)
    
    def __or__(self, other):
        return Or(self, other)
    
    def __invert__(self):
        return Not(self)
    

class FeatureFormula(Formula):
    pass

class FeatureNot(FeatureFormula):
    def __init__(self, operand) -> None:

        if not isinstance(operand, FeatureFormula):
                raise TypeError("Operands must be a feature atom")

        self.operand = operand

    def evaluate(self, datapoint):
        return not self.operand.evaluate(datapoint)
    
    def symbols(self):
        return self.operand.symbols()
    
    def __repr__(self) -> str:
        return f"¬{self.operand}"
    
class FeatureAnd(FeatureFormula):
    def __init__(self, *operands) -> None:
        for op in operands:
            if not isinstance(op, FeatureFormula):
                raise TypeError("Operands must be feature atoms")
        self.operands = operands
    
    def evaluate(self, data_point):
        return all(op.evaluate(data_point) for op in self.operands)
    
    def symbols(self):
        return set.union(*(op.symbols() for op in self.operands))
    
    def __repr__(self) -> str:
        return f"({' ∧ '.join(map(str, self.operands))})"

        
    
class FeatureOr(FeatureFormula):
    def __init__(self, *operands) -> None:
        for op in operands:
            if not isinstance(op, FeatureFormula):
                raise TypeError("Operands must be feature atoms")
            self.operands = operands

    def evaluate(self, data_point):
        return any(op.evaluate(data_point) for op in self.operands)
    
    def symbols(self):
        return set.union(*(op.symbols() for op in self.operands))
    
    def __repr__(self) -> str:
        return f"({ '  ∨ '.join(map(str, self.operands))})"



class ClassificationFormula(Formula):
    pass

class ClassificationNot(ClassificationFormula):
    def __init__(self, operand) -> None:
        if not isinstance(operand, ClassificationFormula):
            raise TypeError("Operand must be a ClassificationFormula")
        self.operand = operand

    def evaluate(self, classification):
        return not self.operand.evaluate(classification)
    
    def symbols(self):
        return self.operand.symbols()
    
    def __repr__(self) -> str:
        return f"¬{self.operand}"
    

class ClassificationAnd(ClassificationFormula):
    def __init__(self, *operands) -> None:
        for op in operands:
            if not isinstance(op, ClassificationFormula):
                raise TypeError("Operands must be ClassificaitonsFornulas")
        self.operands = operands

    def evaluate(self, classification):
        return all(op.evaluate(classification) for op in self.operands)
    
    def symbols(self):
        return set.union(*(op.symbols() for op in self.operands))
    
    def __repr__(self) -> str:
        return f"({ ' ∧ '.join(map(str, self.operands))})"
    

class ClassificationOr(ClassificationFormula):
    def __init__(self, *operands):
        for op in operands:
            if not isinstance(op, ClassificationFormula):
                raise TypeError("Operands must be ClassificationFormulas")
        self.operands = operands
    
    def evaluate(self, classification):
        return any(op.evaluate(classification) for op in self.operands)
    
    def symbols(self):
        return set.union(*(op.symbols() for op in self.operands))
    
    def __repr__(self) -> str:
        return f"({' ∨ '.join(map(str, self.operands))})"

    

        