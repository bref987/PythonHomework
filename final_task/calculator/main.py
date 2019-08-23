import argparse
from calculator.infixConversion import infixToPostfix
from calculator.postfixEvaluation import postfixEval

parser = argparse.ArgumentParser(description='pure-python command-line calculator', prog='pycalc')
parser.add_argument('expression', type=str, help='expression string to evaluate')
args = parser.parse_args()
#print(args.indir)


def main(i=args.expression):
        
    postf = infixToPostfix(i)
    #print (postf)
    print (postfixEval(postf))

        
#if __name__ == "__main__":
#        main(i)
