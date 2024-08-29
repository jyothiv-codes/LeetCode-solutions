class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text)==1:
            return text
        space_count=text.count(" ")
        print("space_count",space_count)
        words=text.split(" ")
        
        while " " in words:
            words.remove(" ")
        while "" in words:
            words.remove("")
        print(words,len(words))
        if len(words)-1>0:
            space_between=int(space_count/(len(words)-1))
        else:
            space_between=0
        print("Space between",space_between)
        final_sentence=""
        for word in words:
            final_sentence+=word
            if space_count>0 and space_count>=space_between:
                final_sentence+= " "*space_between
                space_count-=space_between
            elif space_count>0:
                final_sentence+=" "*space_count
                space_count=0
        if space_count>0:
            final_sentence+=" "*space_count
        print(final_sentence)
        return final_sentence
