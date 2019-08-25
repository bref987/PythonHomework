from calculator.stack_class import Stack
from calculator.operators import operators

def postfix_eval(postfixExpr):

    operand_stack = Stack()
    token_list = postfixExpr.split()

    for token in token_list:
        
        if token not in operators.keys():
            operand_stack.push(int(token)) if token.isdigit() \
                else operand_stack.push(float(token))
        
                
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = operators[token](operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


