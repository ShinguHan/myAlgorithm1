# devide and quanquer

s = [-1,1,2,3,4,5,6,7,8,9]

def location(x,low,high):
    if low > high:
        return -1
    
    mid = (low+high) //2

    if s[mid] == x:
        return mid
    elif s[mid] < x:
        return location(x,mid+1,high)
    elif s[mid] > x:
        return location(x,low, mid-1)
    

result = location(3,1,3)
print(result)
