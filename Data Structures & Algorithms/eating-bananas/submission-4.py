class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles: List[int], k: int, h: int) -> bool:
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return True if time <= h else False
        low: int = 1
        high: int = 0
        for pile in piles:
            high = max(high, pile)
        while low < high:
            mid: int = low + (high - low) // 2
            if check(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        return low


        
        ##lowewr bound would definitely be 1, upper bound would be , if h is less than length of array that is not valid h, so h is the largest pile

        