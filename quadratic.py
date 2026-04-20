# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    raiz= b**2 - 4*a*c
    if raiz > 0:
        x1= (-b + raiz**(1/2))/(2*a)
        x2= (-b - raiz**(1/2))/(2*a)
        return f"({x1}, {x2})"
    elif raiz == 0:
        x1=(-b) / (2*a)
        return f"({x1})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c

def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"
    else:
        return f"f(x) = {a} * X^2 + {c}"


def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {2 * a} * X + {b}"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif a == 0 and b == 0:
        return "f'(x) = 0"
    else:
        return f"f'(x) = {2 * a} * X"