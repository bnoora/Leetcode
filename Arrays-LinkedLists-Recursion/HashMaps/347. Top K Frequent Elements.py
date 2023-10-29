class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [freq[i][0] for i in range(k)]


class Solution2:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        heap = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            for key, value in freq.items():
                heapq.heappush(heap, (-value, key))