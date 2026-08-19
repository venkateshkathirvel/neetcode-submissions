class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        max_r = -1

        for i in range(n-1,-1,-1):

            ans[i] = max_r
            if arr[i] > max_r:
                max_r = arr[i]
            
        return ans