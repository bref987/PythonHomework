from calculator.stack_class import Stack
from calculator.string_parser import parser


def infix_postfix(infixexpr):
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
        "^":  5,
        "abs": 6,
        "round": 6
    }
  
    op_stack = Stack()
    postfix_list = []
    
    token_list = parser(infixexpr)
 
    for token in token_list:
        if token not in prec.keys():
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and \
                                        (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

