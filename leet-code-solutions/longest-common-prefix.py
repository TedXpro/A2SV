class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 300
        count = 0
        common_prefix = ""

        for s in strs:
            if min_len > len(s):
                min_len = len(s)
                common_prefix = s

        for i in range(len(common_prefix)):
            for s in strs:
                if s[i] != common_prefix[i]:
                    return common_prefix[:count]
            count += 1

        return common_prefix[:count]