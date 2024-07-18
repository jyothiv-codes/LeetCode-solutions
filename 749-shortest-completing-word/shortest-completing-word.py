class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def check_freq(word,license_map):
            word_map={}
            for ch in word:
                word_map[ch]=word_map.get(ch,0)+1
            print("word_map",word,word_map)
            for ch in license_map:
                if ch in word_map and word_map[ch]>=license_map[ch]:
                    pass
                else:
                    return False
            return True
        license_list=[]
        for ch in licensePlate:
            if ch.isalpha():
                license_list.append(ch.lower())
        #license_list.sort()
        license_map={}
        for ch in license_list:
            license_map[ch]=license_map.get(ch,0)+1
        license_set=set(license_list)
        print("license set",license_set)
        print("license map",license_map)
        final_ans=[]
        m=0
        for word in words:
            if len(set(word).intersection(license_set))==len(license_set):
                answer=check_freq(word,license_map)
                if answer:
                    final_ans.append(word)
                    if m==0:
                        m=len(word)
                    else:
                        m=min(m,len(word))
        print(final_ans)
        for word in final_ans:
            if len(word)==m:
                return word
        
            


        