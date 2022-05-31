class Logger:

    def __init__(self):
        self.logstream_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(message in self.logstream_dict):           
            if(timestamp-self.logstream_dict[message]>=10):
                self.logstream_dict[message] = timestamp
                return True    
            return False
        elif(message not in self.logstream_dict):
            self.logstream_dict[message]=timestamp
            return True
            