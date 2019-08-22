def filterString(infix):
    nli = ""
    tokenListBef = " ".join(infix).split()
    for i in (range(len(tokenListBef))):

        if (tokenListBef[i] not in "(+-*//^%)"):
            nli += tokenListBef[i]
                
        elif(tokenListBef[i] in "+*-//%") and (tokenListBef[i + 1] in "+*-//%"):
                    
            nli += " " + tokenListBef[i] + tokenListBef[i + 1] + " "
            tokenListBef[i + 1] = ""
        else:
            nli += " " + tokenListBef[i] + " " 
    return nli.split()
