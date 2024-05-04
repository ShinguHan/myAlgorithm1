# 음.. 내가 행렬을 풀다니.. ㅎ 이거 기분 좋다

# 영어 번역
# "음.. 내가 행렬을 풀다니.. ㅎ 이거 기분 좋다"
# 1. 기본적인 번역:

# "Wow, I'm solving matrices... This feels great!"

# 2. 자연스러운 표현:

# "I can't believe I'm actually solving matrices. This is so satisfying!"

# 3. 좀 더 개성 있는 표현:

# "Matrix mastery is my new jam! Feeling like a math whiz!"

# 4. 감탄사 및 어미 활용:

# "Oh my gosh, I'm solving matrices! This is so cool!"

s1 = [[1,2],[3,4]]
s2 = [[2,4],[6,8]] 

n=2
s= [[0]*n for _ in range(n)]
# print(s)

s[0][1] = 2
# print(s)

for i in range(n):
    for j in range(n):
        for k in range(n):
            s[i][j] += s1[i][k]*s2[k][j]

print(s)