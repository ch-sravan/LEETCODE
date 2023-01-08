class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        l=list(sentence)
        l1=set(l)
        return len(l1)==26
