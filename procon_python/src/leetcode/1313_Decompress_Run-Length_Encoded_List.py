class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            ansi=[nums[i+1] for _ in range(nums[i])]
            ans.extend(ansi)
        return ans