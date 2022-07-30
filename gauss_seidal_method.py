

# Gauss seidal method
import numpy as np
A=np.array([[8,-3,2,20],[4,11,-1,33],[1,1,4,9]],dtype=float)
error=0.1
n=len(A)
x=np.empty([n],dtype=float)
while(error>=1.0e-3):
    for i in range(n):
        s=0
        for j in range(n):
            if(j!=i):
                s=s+A[i,j]*x[j]
        t=(A[i,n]-s)/A[i,i]
        error=abs(x[i]-t)
        if(error>=1.0e-3):
            x[i]=t
print("\nsolution of Matrix A: \n",x)
