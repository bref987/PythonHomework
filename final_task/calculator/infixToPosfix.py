from new_package import inputFilter
from new_package import stackClass


def infixToPostfix(infixexpr):
    operators = "(+*-//^%)"
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["%"] = 3
    prec["//"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = stackClass.Stack()
    postfixList = []
    
    tokenList = inputFilter.filterString(infixexpr)
 
    for token in tokenList:
        if token not in operators:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                                        (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)





































