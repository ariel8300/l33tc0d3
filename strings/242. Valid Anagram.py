# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord("a")] += 1
            freq[ord(t[i]) - ord("a")] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False

        return True


print(Solution().isAnagram("rca", "car"))
print(Solution().isAnagram("rar", "car"))
