LINK:https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
  
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1="".join(word1)
        l2="".join(word2)
        return l1==l2
