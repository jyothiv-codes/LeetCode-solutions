import string
class Solution:
    def countValidWords(self, sentence: str) -> int:
        validchars=["abcdefghijklmnopqrstuvwxyz-!.,"]
        words=sentence.split(" ")
        words = [word for word in words if word != ""]
        print(words)
        valid=True
        count=0
        for word in words:
            word=word.strip()
            valid=True
        
            #condition 3
            if '!' in word[0:-1] or '.' in word[0:-1] or ',' in word[0:-1]:
                valid=False
            
            if word.count('!')+word.count('.')+word.count(',')>1:
                valid=False
                
            
            #condition 2;
            if '-' in word:
                index=word.index('-')
                if word.count('-')>1:
                    valid=False
                if index==0 or index==len(word)-1:
                    valid=False
                elif not (word[index-1].isalpha() and word[index-1].islower() and word[index+1].isalpha() and word[index+1].islower()):
                    valid=False
            
            #condition 1:
            if any(char in word for char in "0123456789"):
                valid=False
                
            if valid==True:
                print("word is ",word)
                count+=1
        print(count)
        return count
                 
