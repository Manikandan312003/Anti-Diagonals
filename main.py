def AntiDiagonalOfMatrix(arr):
    M=len(arr)
    for i in range(M-1):                    #Start or upper left
        a=0
        b=i
        while(a<M and b>=0):
            print(arr[a][b],end="\t")
            a,b=a+1,b-1
        print('0\t'*(M-i-1),end="\n")
    for i in range(M):                    #End or lower right
        a=i
        b=M-1
        while(a<M and b>=0):
            print(arr[a][b],end="\t")
            a,b=a+1,b-1
        print('0\t'*(i),end="\n")
(AntiDiagonalOfMatrix([[1,2,3],[4,5,6],[7,8,9]]))