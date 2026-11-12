class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        1. Sort from closest to furthest tie break for speed
        2. Compute arrival times
        3. if stack is empty push the first arrival time onto a stack and add one to fleets
        4. compare the next closest to the top of stack
        5. if next closest is less than top then push and add one
        6. if next closest is greater than or equal top's arrival it joins the fleet
        7. Repeat 3 to 6 until we've processed all cars in the sorted array
        8. return the fleet count
        '''
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i], 0])
 
        cars.sort(reverse=True)
        for car in cars:
            pos = car[0]
            sp = car[1]
            car[2] = (target - pos) / sp
        stack = []
        fleetCount = 0 
        for car in cars: 
            time = car[2]
            if not stack or time > stack[-1]: 
                stack.append(time) 
                fleetCount += 1

        return fleetCount
            


