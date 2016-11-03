# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without
# repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.

# Subscribe to see which companies asked this question


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        present_string = ""
        substring_lenths = [0]
        for index in xrange(len(s)):
            if s[index] not in present_string:
                present_string += s[index]
            else:
                substring_lenths.append(len(present_string))
                repeating_index = present_string.index(s[index])
                present_string = present_string[repeating_index+1:] + s[index]
        substring_lenths.append(len(present_string))
        return max(substring_lenths)


# 982 / 982 test cases passed.
# Status: Accepted
# Runtime: 132 ms

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        present_string = ""
        substring_lenth_max = 0
        for index in xrange(len(s)):
            if s[index] not in present_string:
                present_string += s[index]
            else:
                substring_lenth_max = len(present_string) if len(
                    present_string) > substring_lenth_max else substring_lenth_max
                repeating_index = present_string.index(s[index])
                present_string = present_string[repeating_index+1:] + s[index]
        substring_lenth_max = len(present_string) if len(
            present_string) > substring_lenth_max else substring_lenth_max
        return substring_lenth_max

# 982 / 982 test cases passed.
# Status: Accepted
# Runtime: 105 ms
