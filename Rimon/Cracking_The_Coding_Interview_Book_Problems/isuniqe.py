
s = "strings"
c = 0 
for i in s:
    d = ord(i) - ord('a')
    if(c & 1<<d):
        print("False")
        c = -1
        break
    c  = c | 1<<d 

if c!= -1 :
    print("True")
