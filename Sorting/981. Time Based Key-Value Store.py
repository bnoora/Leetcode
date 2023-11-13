from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                right = mid-1
            else:
                left = mid+1
        
        return arr[right][1] if right >= 0 else ""

        
