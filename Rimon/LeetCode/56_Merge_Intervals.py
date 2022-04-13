class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()
        print(intervals)
        a = intervals[0][0]
        b = intervals[0][1]
        l = []
        for i in intervals:
            if i[0]<= b:
                b = max(b,i[1])
            else:
                l.append([a,b])
                a = i[0]
                b = i[1]
        l.append([a,b])
        # print(l)
        return l
    
       
        # out = [] #collected
        # for i in sorted(intervals, key=lambda i: i[0]):
        #     if out and i[0] <= out[-1][1]:
        #         out[-1][1] = max(out[-1][1], i[1])
        #     else:
        #         out += [i]
        # return out