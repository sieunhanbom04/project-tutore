import NumPy

def extended_euclid_algorithm(a,b):
    if b==0:
        return a,1,0
    d,tempX,tempY=extended_euclid_algorithm(b,a%b)
    x=tempY
    y=tempX-(a/b)*tempY
    return d,x,y
