class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        lis = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        counts = dict(sorted(counts.items(), key=lambda item: item[1]))
        for i in reversed(counts):
            lis.append(i)
            if len(lis) == k:
                return lis


            

        

        