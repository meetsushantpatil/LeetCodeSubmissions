class HitCounter:

    def __init__(self):
        self.list = []    
        self.last_timestamp = 0

    def hit(self, timestamp: int) -> None:
        self.list.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        i = 0
        
        if(timestamp==self.last_timestamp):
            return len(self.list)
        
        while(i<len(self.list)):
            if(timestamp>300):
                if(self.list[i]<=(timestamp-300)): # [1,2,3,4,300]
                    del self.list[i]
                    i-=1
            i+=1
            
        self.last_timestamp = timestamp
        return len(self.list)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


["HitCounter","hit","hit","hit","hit","getHits","hit","getHits","hit","getHits"]
[[],[1],[1],[1],[300],[300],[300],[300],[301],[301]]