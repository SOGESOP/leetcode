
# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle 
# in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask
# during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
import logging
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self) -> None:
        self.output=self.strStr("hello", "ll")
        logging.debug(self.output)

    def strStr(self, haystack: str, needle: str) -> int:
        
 
 
 
 
 
 
    # def strStr(self, haystack: str, needle: str) -> int:
    #     common=""
    #     needle_index=0
    #     index_list=[]
        
    #     # this catches a non entry for needle and returns the correct answer
    #     if needle=="":
    #         return 0
    #     # this checks to see if the needle is in the haystack and adds the parts of it that are
    #     #~ in the haystack
    #     for i in haystack:
    #         if i==needle[needle_index]:
    #             index_list.append(haystack.index(i))
    #             if needle_index<len(needle)-1:
    #                 needle_index+=1
    #             common+=i

    #     # this takes care of the case where the needle is a single letter, and finds its first
    #     #~ occourance
    #     if len(needle)==1:
    #         for i in haystack:
    #             if i==needle[0]:
    #                 return haystack.index(i)
    #     logging.debug(common)
    #     # this take action if some of the needle is in the haystack and some of it isnt
    #     #~ in which case it will return a faliure (-1) as required
    #     if common=="" or common!=needle:
    #         return -1
    #     # this checks to seee if needle was found inside the haystack, and if so return the index
    #     #~ where it is found
    #     if needle==common:
    #         return index_list[0]


instance=Solution()