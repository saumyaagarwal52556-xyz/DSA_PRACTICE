from collections import defaultdict

def groupAnagrams(strs):
        result = defaultdict(list)

        for char in strs:
            sortedChar = "".join(sorted(char))
            result[sortedChar].append(char)

        return list(result.values())