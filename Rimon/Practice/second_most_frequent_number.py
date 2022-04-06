# problem: need to find the highest frequent number and the second highest frequent number
#from given array


def solve_one(l):
    """solved using map/dictionary. And used library function"""
    mp = dict()
    for i in l:
        if i not in mp.keys():
            mp[i] = 1
        else:
            mp[i]+=1
    return sorted(list(mp.values()),reverse=True)[0]  

def solve_two(l):
    #Also return highest and second highest number from an array using single loop
    mp = dict()
    for i in l:
        if i not in mp.keys():
            mp[i] = 1
        else:
            mp[i]+=1
    mx = 0
    mxt = 0 
    for i in mp.values():
        if i > mx:
            mxt = mx 
            mx = i 
        else:
            if i>mxt and i != mx :
                mxt = i
    return [mx,mxt]









l = [5,4,7,8,9,5,4,4,3,5,4,5,7,4]
# print(solve_one(l))
print(solve_two(l))



