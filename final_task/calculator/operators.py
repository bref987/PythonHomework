import math
import operator

def isint(n):
    try:
        int(n)
        return True
    except:
        return False
 
def isfloat(n):
    try:
        float(n)
        return True
    except:
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
    ",": (lambda a,b: (a, b)),
    "^-": (lambda a, b: a ** (-b)),
    "+-": operator.sub,
    "-+": operator.sub,
    "--": operator.add,
    "++": operator.add
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
    "round": (lambda a:  round(a) if (isint(a) or isfloat(a)) \
                                    else round(a[0],a[1])),
    "sin": (lambda a: math.sin(a)),
    "cos": (lambda a: math.cos(a)),
    "pow": (lambda a: math.pow(a[0], a[1])),
    "log": (lambda a: math.log(a) if (isint(a) or isfloat(a)) \
                                    else math.log(a[0],a[1])),
    "log10": (lambda a: math.log10(a) if (isint(a) or isfloat(a)) \
                                    else math.log10(a[0],a[1])),
    "log2": (lambda a: math.log2(a) if (isint(a) or isfloat(a)) \
                                    else math.log2(a[0],a[1])),
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
    "/":  4,
    "//": 4,
    "%":  4,
    "^":  8,
    "abs": 6,
    "round": 6,
    "sin": 6,
    "cos": 6,
    "pow": 6,
    "log": 6,
    "log10": 6,
    "log2": 6,
    "um": 6,
    "^-": 8,
    "--": 3,
    "++": 3,
    "+-": 3,
    "-+": 3
    }
  