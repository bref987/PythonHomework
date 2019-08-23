from calculator.stackClass import Stack
from calculator.stringParser import parser


def infixToPostfix(infixexpr):
#    operators = "(+*-//^%)"
    prec = {
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
        "^":  5  
    }
  
    opStack = Stack()
    postfixList = []
    
    tokenList = parser(infixexpr)
 
    for token in tokenList:
        if token not in prec.keys():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

