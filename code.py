import numpy as np
def spiral(A):
    def rotate(A):
        A=np.array(A)
        y = []
        a=A.shape[0]
        b=A.shape[1]
        for i in range(b):
            o = []
            for j in range(a):
                o.append(A[j][-i - 1])
            y.append(o)
        return np.array(y)
    A=np.array(A)
    t=[]
    h=0
    g=A.shape[0]*A.shape[1]
    q=0
    i=0
    f=0
    while True:
        for j in range(i,A.shape[1]):
            if j==A.shape[1]-(i+1) and i!=j:
                G=rotate(A)
                h+=1
                A=G
                if h == 4:
                    i += 1
                    h = 0
                break
            t.append(A[i][j])
            q+=1
            if q==g:
                f=1
                break
        if f==1:
            break
    return t






# A=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]
# C=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# B=[[1,2,3],[4,5,6],[7,8,9]]
# f=spiral(B)
# k=spiral(A)
# o=spiral(C)
# print(k)
# print(f)



p=[0]*10
p[2:5]=[25]*5
print(p)

queries=[[2,3,603],[1,1,286],[4,4,882]]
print(len(queries))
t=arrayManipulation(10, queries)
print(t)