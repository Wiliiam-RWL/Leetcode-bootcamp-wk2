from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left, right = 0, 0
        counter = Counter()
        while right < len(s):
            ch = s[right]
            counter[ch] += 1
            if counter[ch]==1:
                right += 1
            else:
                max_length = max_length if max_length > right - left else right - left
                while counter[ch] > 1:
                    counter[s[left]] -= 1
                    left += 1
                right += 1
        return max_length if max_length > right - left else right - left 