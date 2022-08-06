class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_dict = {}
        
        for visit in cpdomains:
            
            visit_list = visit.split(" ")
        
            visit_count = int(visit_list[0])
            domains = visit_list[1].split(".")
            
            if(len(domains)==2):
                if(domains[1] not in visit_dict):
                    visit_dict[domains[1]] = visit_count
                else:
                    visit_dict[domains[1]] += visit_count
                    
                if(domains[0]+"."+domains[1] not in visit_dict):    
                    visit_dict[domains[0]+"."+domains[1]] = visit_count
                else:
                    visit_dict[domains[0]+"."+domains[1]] += visit_count
                    
            if(len(domains)==3):
                if(domains[2] not in visit_dict):
                    visit_dict[domains[2]] = visit_count
                else:
                    visit_dict[domains[2]] += visit_count
                    
                if(domains[1]+"."+domains[2] not in visit_dict):    
                    visit_dict[domains[1]+"."+domains[2]] = visit_count
                else:
                    visit_dict[domains[1]+"."+domains[2]] += visit_count
                    
                
                if(domains[0]+"."+domains[1]+"."+domains[2] not in visit_dict):    
                    visit_dict[domains[0]+"."+domains[1]+"."+domains[2]] = visit_count
                else:
                    visit_dict[domains[0]+"."+domains[1]+"."+domains[2]] += visit_count
                    
        result = []
        for key in visit_dict:
            result.append(str(visit_dict[key])+" " + str(key))
            
            
        return result