# /c/d --> {}
# 

class FileSystem:

    def __init__(self):
        self.complete_path = {}

    def createPath(self, path: str, value: int) -> bool:
        
        if(path=="" or path== "/"):
            return False
        
        if(path in self.complete_path):
            return False
        
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.complete_path:
            return False 
         
        self.complete_path[path] = value
        return True
                

    def get(self, path: str) -> int:
        
        if(path in self.complete_path):
            return self.complete_path[path]
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)