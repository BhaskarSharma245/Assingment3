def myreduce(l):
    z = len(lst)
    print(z)
    for i in range(z-1):
        c=l[i]+l[i+1]
        l[i]=l[i+1]
        l[i+1]=c

    return c


if __name__ == "__main__":
    lst=[2,4,6,2,8]
    
    result=myreduce(lst)
    print(result)