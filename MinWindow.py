from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_counter = Counter(t)
        s_counter = Counter()
        left, right = 0, 0
        min_window = ""
        while right < len(s):
            if s[right] in t:
                s_counter[s[right]] += 1
            while False not in [s_counter[ch] >= t_counter[ch] for ch in t]:
                if s[left] not in t:
                    left += 1
                elif s_counter[s[left]] > t_counter[s[left]]:
                    s_counter[s[left]] -= 1
                    left += 1
                else:
                    min_window = (
                        min_window
                        if len(min_window) < right - left + 1  and min_window != ""
                        else s[left : right + 1]
                    )
                    break
            right += 1
        return min_window


obj = Solution()

obj.minWindow("ab", "a")
