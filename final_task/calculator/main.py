from calculator.argparser import parse_args
from calculator.infix_conversion import infix_postfix
from calculator.postfix_evaluation import postfix_eval
from calculator.errors import check_length
from calculator.errors import check_spaces
from calculator.errors import bracket
from calculator.errors import check_digits
from calculator.errors import check_op

def main():    
    input = parse_args()
    if check_length(input):
        input = ""
    if check_spaces(input):
        input = ""
    if bracket(input):
        input = ""
    if check_digits(input):
        input = ""
    if check_op(input):
        input = ""
    if input != "":
        postf = infix_postfix(input)
#    print (postf)
        print(postfix_eval(postf))


"""
if __name__ == "__main__":
        main(i)
"""
