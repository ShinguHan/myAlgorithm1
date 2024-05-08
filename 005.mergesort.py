S =[27, 10, 12, 20,25, 13,15,22,1]

def merge(u,v):
    i=j = 0
    s=[]

    while (i < len(u) and j < len(v)):
        if u[i] > v[j]:
            s.append(v[j])
            j += 1
        else:
            s.append(u[i])
            i += 1

    if i < len(u):
        s += u[i:]
    else:
        s += v[j:]

    return s

def mergesort(s):
    length = len(s)

    if length <= 1:
        return s
    
    mid = length // 2

    u = mergesort(s[0:mid])
    v = mergesort(s[mid:length])

    return merge(u,v)










print('Before:',S)
X =mergesort(S)
print('After:',X)


