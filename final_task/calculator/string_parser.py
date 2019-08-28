from calculator.operators import math_const
from calculator.operators import prec
#from calculator.operators import operators
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
    expression_poly = poly_op(expression_const)
    expression_degree = degree(expression_poly)
    expression_um = unary_op(expression_degree)
    
    return expression_um

def parser_expr(infix):
    oper = "()+-*//^%<<==!=>=>,/-++--+--+^^^^^^^^"
    oper1 =  "+-*//^%<<==!=>=>/-++--+--+^^^^^^^^"
    parse_string = ""
    token_list_bef = " ".join(infix).split()
    for i in (range(len(token_list_bef))):
        if (token_list_bef[i] not in oper) and (token_list_bef[i] not in func):
            parse_string += token_list_bef[i]                
        elif(token_list_bef[i] in oper1) and \
        (token_list_bef[i + 1] in oper1):                    
            parse_string += " " + token_list_bef[i] + token_list_bef[i+1] + " "
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
#            list_um.insert(0, "0")  
        elif list_um[i] == "-" and list_um[i-1] in prec.keys():
            list_um.pop(i)
            list_um.insert(i, "um")
#            list_um.insert(i, "0")
    return list_um

def poly_op(s):    
    sig = ["+-","++","-+","--"]
    lent = 0
    if s[0] in sig:
        s.insert(0, "0")        
    for i in range(len(s)):
        if s[i] in sig and s[i+1] in sig:
            lent += 1
    new_lent = lent + len(s) 
    for i in range(new_lent):        
        if s[i] in sig and s[i+1] in prec.keys():
            s.insert((i+1), "0")        
    return s

def degree(list):
    deg = "^^^^^"
    count = 0
    start = 0
    for i in range(len(list)-2):
        if list[i] in deg and list[i+2] in deg:    
            count += 1
            start = i
        else:
            count += 0
    start += 2
    first_index = start-count*2
    mul = 1

    while count >= 0:
        list[first_index] = "^"*mul
        mul +=1
        first_index += 2
        count -= 1        
    return list