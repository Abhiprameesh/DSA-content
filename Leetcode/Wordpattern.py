class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        ChartoWord = {}
        WordtoChar = {}
        for  c, w in zip(pattern, words):
            if c in ChartoWord and ChartoWord[c] != w:
                return False
            if w in WordtoChar and WordtoChar[w] != c:
                return False
            ChartoWord[c] = w
            WordtoChar[w] = c
        return True        