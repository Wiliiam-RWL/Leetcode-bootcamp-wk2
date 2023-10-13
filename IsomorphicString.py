from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        mapping = dict()
        for i in range(len(s)):
            character = s[i]
            map_t = mapping.get(character, None)
            if map_t is None:
                mapping[character] = t[i]
            elif map_t != t[i]:
                return False
        if len(mapping.values()) > len(set(mapping.values())):
            return False
        return True