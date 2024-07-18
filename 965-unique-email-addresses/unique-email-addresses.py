class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d={}
        for email in emails:
            local,domain=email.split("@")
            if domain not in d:
                d[domain]=[]
            if "." in local:
                local=local.replace(".","")
            if "+" in local:
                local=local.split("+")[0]
            if local not in d[domain]:
                d[domain].append(local)
        count=0
        for key in d:
            for values in d[key]:
                count+=1
        print(count)
        print(d)
        return count
            

        