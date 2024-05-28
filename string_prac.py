# 1768. Merge Strings Alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a=len(word1)
        b=len(word2)
        tot=max([a, b])
        strs=''
        count1,count2=0,0
        for i in range(tot):
            if count1<a:
                strs+=word1[count1]
                count1+=1
            if count2<b:
                strs+=word2[count2]
                count2+=1
        return strs

# 1071. Greatest Common Divisor of Strings
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a    
class Solution(object):

    def gcdOfStrings(self, str1, str2):

        len1 = len(str1)
        len2 = len(str2)

            # Find the GCD of the lengths
        lenCandidate = int(gcd(len1, len2))  
        if len1<len2:
            candidate=str1
        elif len1>len2:
            candidate=str2
        else:
            candidate=str2

        numRepeats = int(len1 / lenCandidate)
        repeatedString = candidate[:lenCandidate] * numRepeats
        print(str1,'=============',repeatedString)
        check1=False
        if str1==repeatedString:
            check1=True
        numRepeats = int(len2 / lenCandidate)
        repeatedString = candidate[:lenCandidate] * numRepeats
        print(str2,'=============',repeatedString)
        check2=False
        if str2==repeatedString:
            check2=True
        if(check2 and check1):
            return candidate[:lenCandidate]
        else:
            return ''
