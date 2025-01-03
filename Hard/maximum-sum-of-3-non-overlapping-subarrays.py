class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        def get_sums(nums, k):
            sums = []
            i = 0
            j = k - 1
            s = 0
            for it in range(i, j+1): s += nums[it]

            while True:
                sums.append(s)
                if j == len(nums) - 1:
                    break
                s -= nums[i]
                j += 1
                i += 1
                s += nums[j]

            return sums
        
        sums = get_sums(nums, k)
        maxs = []
        maxsi = []
        mx = sums[-1]
        mxi = len(sums) - 1
        indx = len(sums) - 1
        for i in reversed(sums):
            if i >= mx:
                mx = i
                mxi = indx
            maxs.insert(0, mx)
            maxsi.insert(0, mxi)
            indx -= 1
        
        maxs2 = []
        maxs2i = []
        ans = sums[-1] + sums[-1-k]
        ansi = (len(sums)-1-k, len(sums)-1)
        maxs2.insert(0, ans)
        maxs2i.insert(0, ansi)
        i = len(sums) -1-k 
        i -= 1
        while i >= 0:
            if sums[i] + maxs[i+k] >= ans:
                ans = sums[i] + maxs[i+k]
                ansi = (i, maxsi[i+k])

            maxs2.insert(0, ans)
            maxs2i.insert(0, ansi)
            i -= 1
        
        maxs3 = []
        maxs3i = []
        ans = sums[-1] + sums[-1-k] + sums[-1-k-k]
        ansi = (len(sums)-1-k-k, len(sums)-1-k, len(sums)-1)
        maxs3.insert(0, ans)
        maxs3i.insert(0, ansi)
        i = len(sums) -1-k-k 
        i -= 1
        while i >= 0:
            if sums[i] + maxs2[i+k] >= ans:
                ans = sums[i] + maxs2[i+k]
                ansi = i, *maxs2i[i+k]
            maxs3.insert(0, ans)
            maxs3i.insert(0, ansi)
            i -= 1
        
        return maxs3i[0]
