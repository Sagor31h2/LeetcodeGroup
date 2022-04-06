#find the highest and the second highest number in a array

l = [5,5,5,5,5,5,6,5,5,5]

mx = 0
mxt = 0
for i in l:
    if i > mx : 
        mxt = mx
        mx = i 
    else:
        if i> mxt and i!=mx :
            mxt = i 
print(mx,mxt)