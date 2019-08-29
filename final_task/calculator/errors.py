from calculator.operators import func
from calculator.operators import operators
from calculator.operators import prec


def check_length(exp):
    if len(exp) == 0:
        print("ERROR: empty input")
        return True
    return False

def check_spaces(exp):
    base = "//>=<!==**"
    ex = exp.split()
    for i in range(len(ex)):
        if ex[i] in base and ex[i+1] in base:
            print("ERROR: lots of spaces")
            return True
    return False

def bracket(expr):
    count_left = 0
    count_right = 0
    ex = " ".join(expr).split()
    for i in ex:
        if i == "(":
            count_left += 1
        elif i == ")":
            count_right += 1
    if count_left != count_right:
        print("ERROR: incorrect brackets")
        return True
    return False

def check_digits(expr):
    ex = expr.split()
    exp = " ".join(expr).split(" ")
    for i in range(len(ex)):
        if ex[i].isdigit() and ex[i+1].isdigit() and ex[i+2].isdigit():
            print("ERROR: incorrect input")
            return True
        elif exp[i] in operators.keys() and exp[i+1] in operators.keys() \
                and exp[i+2] in operators.keys():
            print("ERROR: incorrect input")
            return True
    return False
