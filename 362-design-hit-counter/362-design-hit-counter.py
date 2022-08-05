# O( log n)

class HitCounter:

    def __init__(self):
        self.list = []    

    def hit(self, timestamp: int) -> None:
        self.list.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left, right = 0, len(self.list)-1
        target = timestamp - 300
        
        while(left<=right):
            mid = right-left//2
            if(self.list[mid]<=target):
                left = mid+1
            else:
                right = mid-1
        
        return len(self.list)-left
        
#         while(i<len(self.list)):
#             if(timestamp>300):
#                 if(self.list[i]<=(timestamp-300)): # [1,2,3,4,300]
#                     del self.list[i]
#                     i-=1
#             i+=1
            
#         return len(self.list)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)