import string
import random
store={}
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            characters = string.ascii_letters
            random_string = ''.join(random.choice(characters) for _ in range(8))
            if "http://tinyurl.com/"+random_string not in store:
                store["http://tinyurl.com/"+random_string]=longUrl
                return "http://tinyurl.com/"+random_string
                break
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in store:
            return store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))