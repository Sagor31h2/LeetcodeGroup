t = int(input())
for i in range(t):
    a,b = input().split()
    a = int(a)
    b = int(b)
    
    if b == 0:
        print(a+1)
        continue
    if a == 0:
        print(1)
        continue

    print(b*2 + a +1)
    

