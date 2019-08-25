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
    ",": (lambda a,b: (a, b))
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
                                    else round(a[0],a[1]))
}