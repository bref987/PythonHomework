

from calculator.operators import math_const

def parser(infix_expr):
    expression_list = parser_expr(infix_expr)
    return replace_math_const(expression_list)

def parser_expr(infix):
    operators = "()+-*//^%<<==!=>=>,"
    operators1 = "+-*//^%<<==!=>=>"
    parse_string = ""
    token_list_bef = " ".join(infix).split()
    for i in (range(len(token_list_bef))):

        if (token_list_bef[i] not in operators):
            parse_string += token_list_bef[i]
                
        elif(token_list_bef[i] in operators1) and \
        (token_list_bef[i + 1] in operators1):
                    
            parse_string += " " + token_list_bef[i] + token_list_bef[i + 1] + " "
            token_list_bef[i + 1] = ""
        else:
            parse_string += " " + token_list_bef[i] + " " 
    
    return parse_string.split()

def replace_math_const(list):
    for x in range(len(list)):
            if list[x] in math_const:
                list[x] = str(math_const[list[x]])
    return list
