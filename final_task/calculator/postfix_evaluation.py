from calculator.stack_class import Stack
from calculator.operators import operators
from calculator.operators import func
from calculator.operators import prec
#from calculator.operators import isint
#from calculator.operators import isfloat

def postfix_eval(postfixExpr):


    operand_stack = Stack()
    token_list = postfixExpr.split()
    for token in token_list:
        if token not in prec.keys():
            operand_stack.push(int(token)) if token.isdigit() \
                else operand_stack.push(float(token))     
        else:
            if token in func.keys():
                operand_f = operand_stack.pop()
                res = func[token](operand_f)
                operand_stack.push(res)
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = operators[token](operand1, operand2)
                operand_stack.push(result)
    return operand_stack.pop()
