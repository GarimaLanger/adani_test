import numpy as np
import random

def s2dlist(l1,ci1):
    l2=sorted(l1,key=lambda x:x[ci1])
    print(l2)

def c2dlist(numberOfRows,numberOfColumns):
    l=np.random.randint(0, 100, size=(numberOfRows,numberOfColumns))
    print(l)
    ci=int(input("Enter the column index: "))
    s2dlist(l,ci)
    
def main():
    nr=int(input("Enter the number of rows: "))
    nc=int(input("Enter the number of columns: "))
    c2dlist(nr,nc)
    
if 'name' == "main":
    print(main())