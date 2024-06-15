class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d={}
        for domain in cpdomains:
            count,subdomain=domain.split(" ")
            while "." in subdomain:
                d[subdomain]=d.get(subdomain,0)+int(count)
                index=subdomain.index(".")
                subdomain=subdomain[index+1:]
            d[subdomain]=d.get(subdomain,0)+int(count)
                    
                
        answer=[]
        for key in d:
            pair=str(d[key])+" "+key
            answer.append(pair)
        return answer

            
        