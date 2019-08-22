from new_package import stackClass

def postfixEval(postfixExpr):
    operators = "+-*//^%"
    operandStack = stackClass.Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token not in operators:
            operandStack.push(int(token)) if ("." not in token) \
                else operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            
            result = doMath(token, operand1, operand2)
            
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "^": 
        return op1 ** op2
    elif op == "*": 
        return op1 * op2 
    elif op == "/":
        return op1 / op2
    elif op == "%": 
        return op1 % op2 
    elif op == "//":
        return op1 // op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
