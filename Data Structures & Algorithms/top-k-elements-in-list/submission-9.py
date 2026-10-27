class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        result = []
        maxi = 0
        for i in nums:
            if i in mydict:
                mydict[i] = mydict[i] + 1
            else:
                mydict[i] = 1
        for j in range(k):
            maxi = 0
            for key, freq in mydict.items():
                if freq > maxi:
                    maxi = freq
                    target = key
            result.append(target)
            del mydict[target]
        return result
                