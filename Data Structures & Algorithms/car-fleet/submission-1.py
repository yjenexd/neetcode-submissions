class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        res = []
        for i in range (len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse = True, key = lambda x: x[0]) #sort in descending based on the position O(nlog(n))
        print(cars)
        times = list(map(lambda x: (target - x[0]) / x[1], cars)) ##map is a python function that returns an object that needs to be converted to list
        print(times)
        for time in times:
            if not res:
                res.append(time)
            elif time > res[-1]:
                res.append(time)
        return len(res)



        
##[1,4], [4,6], [7,8], [10,10], so the output is 1 fleet
#[4,1,0,7], [6,3,1,8], [8,5,2,9], [10, 7, 3, 10] 3 fleets

##thinking in the fact that it is a one way road, it makes sense that the first car should be at the bottom of the stack


##sort the cars in reversed order based on their position
##map the position such that it corresponds to the time taken to reach the destination
##for each timing that is less than the timing on top of the stack, add the timing to the stack
##return the length of the stack