
def parser(infix):
    operators = "()+-*//^%<<==!=>=>"
    operators1 = "+-*//^%<<==!=>=>"
    nli = ""
    tokenListBef = " ".join(infix).split()
    for i in (range(len(tokenListBef))):

        if (tokenListBef[i] not in operators):
            nli += tokenListBef[i]
                
        elif(tokenListBef[i] in operators1) and (tokenListBef[i + 1] in operators1):
                    
            nli += " " + tokenListBef[i] + tokenListBef[i + 1] + " "
            tokenListBef[i + 1] = ""
        else:
            nli += " " + tokenListBef[i] + " " 
    return nli.split()
