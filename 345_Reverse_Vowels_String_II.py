class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=[i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        temp=list(s)
        for i in range(len(vowels)//2):
            temp[vowels[i]],temp[vowels[-i-1]]=temp[vowels[-i-1]],temp[vowels[i]]
        return "".join(temp)

        # vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        # s1 = list(s)
        # for i in range(len(vowels)//2):
        #     s1[vowels[i]], s1[vowels[-i-1]] = s1[vowels[-i-1]], s1[vowels[i]]
        # return ''.join(s1)
        # temp=[]
        # res=""
        # start=0
        # end=len(s)-1
        # for item in s:
        #     temp+=item
        # while start<end:
        #     if temp[start] not in "aeiouAEIOU":
        #         start +=1
        #     if temp[end] not in "aeiouAEIOU":
        #         end -=1
        #     if temp[start] in "aeiouAEIOU" and temp[end] in "aeiouAEIOU":
        #         temp[start],temp[end]=temp[end],temp[start]
        #         start +=1
        #         end -=1
        # for i in temp:
        #     res+=i
        # print(res)

s = "A man, aPanama"
b=Solution()
b.reverseVowels(s)