class MyCalendar:

    def __init__(self):
        self.event_list = []

    def book(self, start: int, end: int) -> bool:
        
        if(len(self.event_list)==0):
            self.event_list.append([start,end])
            return True
        else:
            for start_temp,end_temp in self.event_list:
                if(start>=start_temp and start<end_temp):
                    return False
                elif(end>start_temp and end<=end_temp):
                    return False
                elif(start<start_temp and end>end_temp):
                    return False
            
            self.event_list.append([start,end])
            return True
            
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)  10,20
# param_1 = obj.book(start,end)  15,25
