# {"daniel" : [10:00, 10:05, 10:10]}

from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        log = defaultdict(list)
        result = []
        
        for i in range(len(keyName)):
            log[keyName[i]].append(int(keyTime[i][0:2]+keyTime[i][3:5]))
            
        
        for key in log:
            log[key].sort()
            for i in range(2, len(log[key])):
                if log[key][i] - log[key][i-2] <= 100:
                    result.append(key)
                    break
        
        result.sort()
        return result
                