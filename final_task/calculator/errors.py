def check_length(exp):
    if len(exp) == 0:
        print("ERROR: empty input")
        return True
    return False

def check_spaces(exp):
    base = "//>=<!=="
    ex = exp.split()
    for i in range(len(ex)):
        if ex[i] in base and ex[i+1] in base:
            print("ERROR: lots of spaces")
            return True
    return False
