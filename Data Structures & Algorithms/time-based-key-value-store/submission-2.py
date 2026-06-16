class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list) ##initialize a dict
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        if not values:
            return ""
        low = 0
        high = len(values)
        res = ""
        while low < high:
            mid = low + (high - low) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                low = mid + 1
            else:
                high = mid
        return res