t = int(input())
for i in range(t):
    n = int(input())
    mxa = 0 
    mxb = 0
    k = input().split()
    # print(k)
    k = [int(i) for i in k]
    k = sorted(k)
    # print(k)
    mxa = 0
    mxb = 0
    for i in k:
        if i>=mxa:
            mxb = mxa
            mxa = i 
    
    if mxa - mxb > 1:
        print("NO")
    else:
        print("YES")
