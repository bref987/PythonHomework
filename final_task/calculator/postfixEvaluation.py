from calculator.stackClass import Stack

operators = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
    "//": (lambda a, b: a // b),
    "^": (lambda a, b: a ** b),
    "%": (lambda a, b: a % b),
    "<": (lambda a, b: a < b),
    "<=": (lambda a, b: a <= b),
    "==": (lambda a, b: a == b),
    "!=": (lambda a, b: a != b),
    ">=": (lambda a, b: a >= b),
    ">": (lambda a, b: a > b)
}

def postfixEval(postfixExpr):

    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token not in operators.keys():
            operandStack.push(int(token)) if ("." not in token) \
                else operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operators[token](operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


