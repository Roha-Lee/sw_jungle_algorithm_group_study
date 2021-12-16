class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # drop non-alpha characters, make lower case
        words = re.sub('[^a-z]', ' ', paragraph.lower()).split()
        word_count = {}
        
        # count words
        for word in words:
            if word in banned:
                continue
                
            if not word in word_count:
                word_count[word] = 0
            
            word_count[word] += 1
            
        # get key with max value
        return (max(word_count,key=word_count.get))