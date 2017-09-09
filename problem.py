from random import randint
import matplotlib
import matplotlib.pyplot as plt

def generate(k,h, returnBits = False) :
    l=[]
    for i in range(h) :
        x=randint(0,k)
        while x in l :
            x=randint(0,k)
        l.append(x)
    sum=0
    for i in l :
        sum+= 2**i
    if not returnBits:
        return sum
    else:
        return l, sum
    
def generate_problem(k,h) :
    A=generate(k,h)
    B=generate(k,h)
    X=generate(k,h)
    Y=generate(k,h)
    C=(A*X+B*Y)%(2**k-1)
    return A,B,C,X,Y
    

def hamming_weight(n) :
    t=0
    while n>0 :
       t+=n%2
       n//=2
    return t
    
    
def testPlot(k, h):
    A,B,C,X,Y = generate_problem(k,h)
    A=generate(k,h)
    B=generate(k,h)
    Xl, X=generate(k,h, returnBits = True)
    Y=generate(k,h)
    n = 2**k-1
    C=(A*X+B*Y)%n
    lst = [hamming_weight(C)]
    for p in Xl:
        C = (C -  2 ** p * A) % n
        lst.append(hamming_weight(C))
    plt.plot(list(range(h + 1)), lst)
    plt.show()
    
def backtrack(A,B,C,h,k,n,result,p):
    if p == k:
        return False, None
    elif len(result) == h:
        return 
    if hamming_weight(newC)==hamming_weight(C)-h:
        newC=(C -  2 ** p * A) % n
        
        #backtrack(A,B
        
    
     

            