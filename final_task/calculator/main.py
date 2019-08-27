import argparse
from calculator.infix_conversion import infix_postfix
from calculator.postfix_evaluation import postfix_eval

parser = argparse.ArgumentParser(
            description='pure-python command-line calculator', prog='pycalc')
parser.add_argument('expression', type=str, 
                    help='expression string to evaluate')
args = parser.parse_args()

def main(i=args.expression):
        
    postf = infix_postfix(i)
    print (postf)
    print (postfix_eval(postf))
        
#if __name__ == "__main__":
#        main(i)
