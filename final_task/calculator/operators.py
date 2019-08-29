import math
import operator


def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "^": operator.pow,
    "%": operator.mod,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
    ",": (lambda a, b: (a, b)),
    "^-": (lambda a, b: a ** (-b)),
    "+-": operator.sub,
    "-+": operator.sub,
    "--": operator.add,
    "++": operator.add,
    "^^": operator.pow,
    "/-": (lambda a, b: a / -b)
}

math_const = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
    "nan": math.nan
}

func = {
    "abs": abs,
    "round": (
            lambda a: round(a) if (isint(a) or isfloat(a))
            else round(a[0], a[1])),
    "sin": (lambda a: math.sin(a)),
    "cos": (lambda a: math.cos(a)),
    "pow": (lambda a: math.pow(a[0], a[1])),
    "log": (lambda a: math.log(a[0], a[1]) if isinstance(a, tuple)
            else math.log(a)),
    "log10":(lambda a: math.log(a[0], a[1]) if isinstance(a, tuple)
            else math.log(a)),
    "log2": (lambda a: math.log(a[0], a[1]) if isinstance(a, tuple)
            else math.log(a)),
    "um": (lambda a, b=0: b - a)
}

prec = {
    ",": 1,
    "(":  0,
    ")":  0,
    "==": 1,
    "!=": 1,
    "<":  2,
    ">=": 2,
    ">":  2,
    "<=": 2,
    "+":  3,
    "-":  3,
    "*":  4,
    "/-": 4,
    "/":  4,
    "//": 4,
    "%":  4,
    "^":  5,
    "abs": 7,
    "round": 7,
    "sin": 7,
    "cos": 7,
    "pow": 7,
    "log": 7,
    "log10": 7,
    "log2": 7,
    "um": 6,
    "^-": 6,
    "--": 3,
    "++": 3,
    "+-": 3,
    "-+": 3,
    "^^": 6
    }
