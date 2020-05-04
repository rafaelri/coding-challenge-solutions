class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub = set(s[0])
        lg = 1
        curr = s[0]
        for i in range(1, len(s)):
            c=s[i]
            if not c in sub:
                sub.add(c)
                curr = curr + c
                if len(curr)>lg:
                    lg = len(curr)
            else:
                r = curr[0]
                while curr:
                    sub.remove(r)
                    curr = curr[1:]
                    r = curr[0]
                sub.add(c)
        return lg

print(Solution().lengthOfLongestSubstring("dvdf"))