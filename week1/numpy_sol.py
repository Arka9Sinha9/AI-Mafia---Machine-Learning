##import numpy
import numpy as np

#print version and configuration
print(np.__version__)
print(np.show_config())

#create null vector of size 10
ten=np.zeros(10)
print(ten)

#print memory size of arrays
print(ten.itemsize)

#documentation of numpy add function
#python -c "import numpy; numpy.info(numpy.add)"

#create a null vector of size 10 but 5th value is 1
a=np.zeros(10)
a[4]=1
print(a)

#create a vector with values ranging from 10 to 49
b=np.arange(10,50)
print(b)

#reverse a vector
c=b[::-1]
print(c)

#create a 3*3 matrix with values from 0 to 8
d=np.arange(0,9)
d=d.reshape(3,3)
#or d=np.arange(0,9).reshape(3,3)
print(d)

#find indices of non zero numbers
e=np.nonzero([1,2,0,0,4,0])
print(e)

#create a 3*3 identity matrix
f=np.eye(3)
print(f)

#create a 3*3*3 array with random values
g=np.random.random((3,3,3))
print(g)

#create a 10*10 array with random values and find max and min
h=np.random.random((10,10))
print(h)
print(h.max())
print(h.min())

#create a random vector of size 30 and find mean value
i=np.random.random((30))
print(i)
print(i.mean())

#create a 2d array with 1 on the border and 0 inside
j=np.ones((5,5))
j[1:-1,1:-1]=0
print(j)

#how to add a border(filled with 0s) around an existing array
k=np.random.random((5,5))
l=np.pad(k,pad_width=1,mode='constant',constant_values=0)
print(l)

print(0*np.nan)#nan
print(np.nan==np.nan)#false
print(np.inf>np.nan)#false
print(np.nan-np.nan)#nan
print(np.nan in set([np.nan]))#true
print(0.3==3*0.1)#false

#create a 5*5 matrix with values 1,2,3,4 just below the diagonal
m=np.diag(1+np.arange(4), k = -1)#k=-1 for below diagonal and +1 for above
print(m)

#create a 8*8 matrix and fill it with chessboard pattern
n=np.zeros((8,8),dtype=int)
n[1::2,::2]=1
n[::2,1::2]=1
print(n)

#consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
o=np.unravel_index(100,(6,7,8))
print(o)
