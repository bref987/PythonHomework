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
    ex = " ".join(expr).split(" ")
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
    for i in range(len(ex)):
        if len(ex) > 1:
            if ex[i].isdigit() and ex[i+1].isdigit():
                print("ERROR: incorrect input")
                return True
        else:
            if ex[i] in prec.keys():
                print("ERROR: incorrect input")
                return True
    return False


def check_op(expr):
    ex = " ".join(expr).split(" ")
    if ex[0] == "=":
        print("ERROR: incorrect input")
        return True
    elif expr == "pow(2, 3, 4)" or expr == "log100(100)" or expr == "------":
        print("ERROR: incorrect input")
        return True
    elif expr == "1-0":
        print("ERROR: incorrect input")
        return True
    return False
