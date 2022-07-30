# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:46:35 2022

@author: Rakin Shahriar
"""


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        new_list = []
        words2 = sorted(words2)
        for i in words1:
            j = sorted(i)
            for k in j:
                for l in words2:
                    if l in j:
                        new_list.append(i)


        return new_list

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
t = Solution()
t_obj = t.wordSubsets(words1,words2)
print(t_obj)