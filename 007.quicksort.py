S = [4,6,1,43,9,3,26,7,34,2341,234]

# S= [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]

def partition(S, low, high):
    point = S[low]
    i,j = low+1,high

    while(i<=j):
        while(S[i]<point and i<len(S)):
            i+=1
        while(S[j]>point):
            j-=1
        if(i<j):
            S[i],S[j]=S[j],S[i]
    
    pivot = j

    S[low], S[pivot] = S[pivot], S[low]

    return pivot

def quicksort(S, low, high):
    if high > low:
        pivot = partition(S,low, high)
        quicksort(S, low, pivot-1)
        quicksort(S,pivot+1, high)

print('Before: ',S)
quicksort(S,0,len(S)-1)
print('After: ',S)
