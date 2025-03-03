class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def calc_freq(word):
            freq={}
            for ch in word:
                freq[ch]=freq.get(ch,0)+1
            to_return=sorted(freq)
            #print("sorted dict",to_return)
            return_string=""
            for key in to_return:
                return_string+=key
                return_string+=str(freq[key])
            return str(return_string)

        d={}
        for word in strs:
            possible_key=calc_freq(word)
            if possible_key not in d:
                d[possible_key]=[]
            d[possible_key].append(word)
        answer=[]
        for key in d:
            answer.append(d[key])
        return answer




        