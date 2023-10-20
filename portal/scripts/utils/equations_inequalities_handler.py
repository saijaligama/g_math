import sympy as sp

def calculate_equation(equation_or_inequality_str):
    # print(eqn)
    x = sp.symbols('x')
    if '=' in equation_or_inequality_str:
        sides = equation_or_inequality_str.split('=')
        left_side = sp.sympify(sides[0].strip())
        right_side = sp.sympify(sides[1].strip())
        equation = sp.Eq(left_side, right_side)
        solutions = sp.solve(equation, x)
    else:
        inequality = sp.sympify(equation_or_inequality_str)
        solutions = sp.solve_univariate_inequality(inequality, x, relational=False)

    return str(solutions)