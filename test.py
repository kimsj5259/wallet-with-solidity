# def romanToInt(s):
#         roman2value = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}

#         value = 0
#         temp=''
#         cursor=0
#         while cursor<len(s):
#             if (cursor+1)!=len(s) and s[cursor]+s[cursor+1] in roman2value:
#                 value += roman2value[s[cursor]+s[cursor+1]]
#                 print(value)
#             else:
#                 value+=roman2value[s[cursor]]
#                 cursor+=1
#                 print(cursor)
        
#         return value

# print(romanToInt('LVIII'))

from multiprocessing.sharedctypes import Value
from optparse import Values


def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0

        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
            
        return z + roman[s[-1]]

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        letter_at_index = ""
        final_string = ""
    
        length_of_string = len(strs[0])

        
        # for index_in_strs in range(0, length_of_string):
        #     for index_in_list_of_strs, string in enumerate(strs):
        #         if index_in_list_of_strs == 0:
        #             letter_at_index = string[index_in_strs]
        #         elif string[index_in_strs] != letter_at_index:
        #             return final_string
        #         else:
        #             pass
            
        #     final_string += letter_at_index
        #     letter_at_index = ""
        
        # return final_string
        a = map(lambda x: x**2, range(5))
        print(a)
        from functools import reduce
        b= reduce(lambda x,y: y+x, 'abcde')
        c= reduce(lambda x,y: y+x, [0,1,2,3])
        

print(Solution().longestCommonPrefix(["jin", "kim", "sung"]))