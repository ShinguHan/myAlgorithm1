# MergeSort 2

def merge2(S,low, mid, high):
    U=[]
    i=low
    j=mid+1

    # print("id:",id(S))

    while (i<=mid and j<= high):
        if(S[i] <S[j]):
            U.append(S[i])
            i+= 1
        else:
            U.append(S[j])
            j+= 1
    if(i<=mid):
        U+=S[i:mid+1]
    else:
        U+=S[j :high +1]
    for k in range(low, high +1):
        S[k]=U[k-low] 

    # print("id:",id(S))
    

def mergesort2 (S, low, high):
    if (low <high):
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        print("S1:",S)
        mergesort2(S, mid + 1, high)
        print("S2:",S)

        merge2(S, low, mid, high)
        print("S3:",S)


# S =[27, 10, 12, 20,25, 13,15,22]
S =[27, 10,11]

# print("id:",id(S))
print('Before:',S)
mergesort2(S, 0, len(S)-1)
print('After:',S)