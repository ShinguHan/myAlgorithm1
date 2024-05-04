# I try to solve algorithm problem by myself. I think it is meaningful action for me

s= [3,7,1,32,6,132]

for i in range(len(s)-1):
    print("List S: ",s)

    for j in range(i+1, len(s)):
        if s[i] > s[j]:
            s[i],s[j] = s[j],s[i]

print("Final:",s)