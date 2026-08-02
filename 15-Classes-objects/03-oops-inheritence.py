import math

class ScientificCalculator:

    def cos(self, n):
        return math.cos(n)

# Inheritence, Calculator is inheriting properties/methods from ScientificCalculator.
class Calculator(ScientificCalculator):

    def add(self, n1, n2):
        return n1 + n2
    

calc = Calculator()

sum = calc.add(1, 3)
cos_v = calc.cos(2)
print(sum)
print(cos_v)
#scalc = ScientificCalculator()

#scalc.cos(2)