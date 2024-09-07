class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""
        for ch in s:
            if ch==' ':
                print(word)
                words.append(word)
                word=""
            else:
                word+=ch
        words.append(word)
        words=words[::-1]
        print(words)
        output_s=""
        for word in words:
            if word!='':
                output_s+=word
                output_s+=" "
        return output_s[:-1]
        