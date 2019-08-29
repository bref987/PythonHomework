from calculator.argparser import parse_args
from calculator.infix_conversion import infix_postfix
from calculator.postfix_evaluation import postfix_eval
from calculator.errors import check_length
from calculator.errors import check_spaces


def main():    
    input = parse_args()
    if check_length(input):
        input = ""
    if check_spaces(input):
        input = ""
    if input != "":
        postf = infix_postfix(input)
#    print (postf)
        print(postfix_eval(postf))


"""
if __name__ == "__main__":
        main(i)
"""
