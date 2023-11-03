import math
import re

def solve_log_equation(expression):
    tokens = re.findall(r'log\(\d+\)', expression)
    for token in tokens:
        num = int(token[4:-1])
        expression = expression.replace(token, str(math.log(num)))
    return eval(expression)