a=['x','y','z']

lst=[i*j for i in a for j in range(1,5)]
print(lst)
print()

lst=[i*j for i in range(1,5) for j in a]
print(lst)
print()


lst=[[j+i] for i in range(3) for j in range(2,5)]
print(lst)
print()

lst=[[j+i for i in range(4)] for j in range(2,6)]
print(lst)
print()

lst=[(i,j) for i in range(1,4) for j in range(1,4)]
print(lst)
