from math import *
from sympy import *
from matplotlib import pyplot as pa
def gph(q,i):
    xa=[]
    y=[]
    xa.append(i-0.3)
    xa.append(i+0.3)
    x=i-0.3
    j=eval(q)
    x=i+0.3
    k=eval(q)
    lm=sqrt(j**2+k**2)
    #y.append(j/lm)
    #y.append(k/lm)
    pa.plot(xa,y,"b-")
def eqa(q,n):
    l=[]
    xv=[]
    xvj=[]
    for i in range(-n,n+1):
        for j in range(-n,n):
            xv.append(i)
            xvj.append(j)
            x=i
            y=j
            l.append(eval(q))
    ln=len(xv)
    c=[]
    for i in range(ln-1):
        k=xvj[i]-(l[i]*xv[i])
        c.append(k)
    return (xv,xvj,l,c)
def df(f):
    l=[]
    x=float(input("enter the x value:-"))
    y=float(input("enter the y value:-"))
    n=int(input("enter the no of values:-"))
    h=float(input("enter the step size:-"))
    fa=eval(f)
    xv=[]
    xv.append(x)
    l.append(fa)
    for i in range(n):
        xv.append(x)
        x=x+h
        y=fa
        fa=fa+h*(eval(f))
        l.append(fa)
    print(l,"\n",xv)
    pa.plot(xv,l,"r-",label="diff")
def sf(xv,xvj,l,c):
    ln=len(c)
    for i in range(ln):
        x=symbols('x')
        h=l[i]*x+c[i]
        h=str(h)
        gph(h,xv[i])
while 1:
    q=input("enter the exp:=")
    n=int(input("enter the range:="))
    xv,xvj,l,c=eqa(q,n)
    sf(xv,xvj,l,c)
    #df(q)
    pa.show()
    #h,xv,l2=df()
    #pa.show()
