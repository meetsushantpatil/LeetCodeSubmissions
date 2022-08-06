class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_dict = {}
        
        for visit in cpdomains:
            
            visit_list = visit.split(" ")
        
            visit_count = int(visit_list[0])
            domains = visit_list[1].split(".")
            
            for i in range(len(visit_list[1])-1,-1,-1):
                domain_indv = ""
                
                if(visit_list[1][i]=="."):
                    domain_indv = visit_list[1][i+1:len(visit_list[1])]
                    
                if(i==0):
                    domain_indv = visit_list[1]
                
                if(domain_indv not in visit_dict and domain_indv!=""):
                    visit_dict[domain_indv] = visit_count
                elif(domain_indv in visit_dict):
                    visit_dict[domain_indv] += visit_count
            
#             if(len(domains)==2):
#                 if(domains[1] not in visit_dict):
#                     visit_dict[domains[1]] = visit_count
#                 else:
#                     visit_dict[domains[1]] += visit_count
                    
#                 if(domains[0]+"."+domains[1] not in visit_dict):    
#                     visit_dict[domains[0]+"."+domains[1]] = visit_count
#                 else:
#                     visit_dict[domains[0]+"."+domains[1]] += visit_count
                    
#             if(len(domains)==3):
#                 if(domains[2] not in visit_dict):
#                     visit_dict[domains[2]] = visit_count
#                 else:
#                     visit_dict[domains[2]] += visit_count
                    
#                 if(domains[1]+"."+domains[2] not in visit_dict):    
#                     visit_dict[domains[1]+"."+domains[2]] = visit_count
#                 else:
#                     visit_dict[domains[1]+"."+domains[2]] += visit_count
                    
                
#                 if(domains[0]+"."+domains[1]+"."+domains[2] not in visit_dict):    
#                     visit_dict[domains[0]+"."+domains[1]+"."+domains[2]] = visit_count
#                 else:
#                     visit_dict[domains[0]+"."+domains[1]+"."+domains[2]] += visit_count
                    
        result = []
        for key in visit_dict:
            result.append(str(visit_dict[key])+" " + str(key))
            
            
        return result