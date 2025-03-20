class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        ans=""
        split_sentence=sentence.split(" ")
        for word in split_sentence:
            if word[0]=="$" and word[1:].isdigit():
                price=int(word[1:])
                price=round(price-(discount*price/100),2)
                price = "{:.2f}".format(price)
                price="$"+str(price)
                ans+=price
            else:
                ans+=word
            ans+=" "
        return ans[:-1]

        