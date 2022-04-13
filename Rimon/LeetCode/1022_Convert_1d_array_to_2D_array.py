class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = []
        t = []
        k = 0
        if len(original) != m * n:
            return []
        for i in original:
            t.append(i)
            k+=1
            if(k==n):
                l.append(t.copy())
                k = 0
                t = []
                continue
            
            
        print(l)
        return l
    
        # optimal solution
        # public int[][] construct2DArray(int[] original, int m, int n) {
        #     if(original.length != m*n) return new int[0][0];
        #     int[][] result = new int[m][n];
        #     for(int i=0;i<original.length;i++)
        #         result[i/n][i%n] = original[i];
        #     return result;
        # }