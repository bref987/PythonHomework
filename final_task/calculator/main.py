from calculator.argparser import parse_args
from calculator.infix_conversion import infix_postfix
from calculator.postfix_evaluation import postfix_eval

def main():
    input = parse_args() 
    postf = infix_postfix(input)
#    print (postf)
    print (postfix_eval(postf))
        
if __name__ == "__main__":
        main(i)