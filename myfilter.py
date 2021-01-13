def marks(n):
    if n>=50:
        return True


def myfilter(b,marks):
    result=list()
    for i in b:
        if marks(i):
            result.append(i)
    
    return result
    
    

if __name__ == "__main__":
    a=[10,30,50,74,35,98,55]
    print(myfilter(a,marks))