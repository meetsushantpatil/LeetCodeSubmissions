class Solution: # worst case time o(nlogn) - position range n nodes and speed*2 every time so logn
    def racecar(self, target: int) -> int: # space o(nlogn) because number of nodes in graph matches time    
        queue, visited = [], set()
        position, speed, count = 0, 1, 0
        queue.append([position, speed, count])
        while queue: # bfs with pruning
            p, s, c = queue.pop(0)
            if (p, s) in visited: # if visited same position with same speed
                continue # skip searching it
            if p == target: # if reached target
                return c # return count
            visited.add((p, s)) # add new state to visited set
            if abs(target-(p+s)) < target: # if the next position does not further us from the target
                queue.append([p+s, s*2, c+1]) # then keep the car in the direction it is going
            if p+s > target and s > 0: # if car passed the target and moving forward
                s = -1 # then change the direction of the car
                queue.append([p, s, c+1]) # add new point
            elif p+s < target and s < 0: # if car before the target and moving away in reverse
                s = 1 # then change the direction of the car
                queue.append([p, s, c+1]) # add new point