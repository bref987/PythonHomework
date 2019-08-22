import argparse
from new_package import infixToPosfix
from new_package import postfixEvaluation

parser = argparse.ArgumentParser(description='test')
parser.add_argument('indir', type=str, help='inp')
#parser.add_argument('outdir', type=int, help='Output dir for image')
args = parser.parse_args()
#print(args.indir)


def main(i=args.indir):
        
    postf = infixToPosfix.infixToPostfix(i)
    print (postf)
    print (postfixEvaluation.postfixEval(postf))

        
#if __name__ == "__main__":
#        main(i)

