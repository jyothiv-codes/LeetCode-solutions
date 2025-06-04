class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        hours=3600
        minutes=60
        store={}
        for access in access_times:
            employee,time=access[0],access[1]
            if employee not in store:
                store[employee]=[]
            h,m=time[0:2],time[2:]
            h,m=int(h),int(m)
            total_time=h*hours+(m*minutes)
            store[employee].append(total_time)

        
        for key in store:
            store[key].sort()
        print(store)
        output=[]
        for key in store:
            if len(store[key])>=3:
                temp=[store[key][0]]
                i=1
                while i<len(store[key]):
                    if len(temp)==3:
                        break
                    if store[key][i]-temp[0]<3600:
                        temp.append(store[key][i])
                    else:
                        temp.pop(0)
                        temp.append(store[key][i])
                    i+=1
                print("temp is ",temp,key)
                if len(temp)>2:
                    output.append(key)
            
        return output

        