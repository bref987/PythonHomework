from calculator.operators import math_const
from calculator.operators import prec
from calculator.operators import operators
from calculator.operators import func

def tostring(l):
    string = ""
    for i in l:
        string += i
        string += " "
    return string

def parser(infix_expr):
    expression_list = parser_expr(infix_expr)
    expression_const = replace_math_const(expression_list)
    expression_um = unary_op(expression_const)
    
    return expression_um
    

def parser_expr(infix):
    operators = "()+-*//^%<<==!=>=>,/-"
    operators1 = "+-*//^%<<==!=>=>/-"
    parse_string = ""
    token_list_bef = " ".join(infix).split()
    for i in (range(len(token_list_bef))):

        if (token_list_bef[i] not in operators):
            parse_string += token_list_bef[i]
                
        elif(token_list_bef[i] in operators1) and \
        (token_list_bef[i + 1] in operators1):
                    
            parse_string += " " + token_list_bef[i] + token_list_bef[i + 1] + " "
            token_list_bef[i + 1] = " "
        else:
            parse_string += " " + token_list_bef[i] + " " 
    
    return parse_string.split()

def replace_math_const(list):
    for x in range(len(list)):
            if list[x] in math_const:
                list[x] = str(math_const[list[x]])
    return list


def unary_op(list_um):
    for i in range(len(list_um)):
        if list_um[i] == "-" and i == 0:
            list_um.pop(0)
            list_um.insert(0, "um")
            list_um.insert(0, "0")  
        elif list_um[i] == "-" and list_um[i-1] in prec.keys():
            list_um.pop(i)
            list_um.insert(i, "um")
            list_um.insert(i, "0")
    return list_um



"""def unary_op(exv):
    exp_bef = parser_expr(exv)
    op =  "()+-*//^%<<==!=>=>,"
    exp = " ".join(exp_bef).split()
    for i in range(len(exp)):
        if exp[i] == "-" and i == 0:
            exp.pop(0)
            exp.insert(0, "um ")
            exp.insert(0, " 0 ")
            
        elif exp[i] == "-" and exp[i-1] in op:
            exp.pop(i)
            exp.insert(i, "um")
            exp.insert(i, "0")
    return " ".join(parser_expr(exp)).split()

"""