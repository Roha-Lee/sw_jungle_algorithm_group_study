from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')
        words = [word for word in paragraph.lower().split() if word not in banned]
        counter = Counter(words)
        return counter.most_common()[0][0]
        