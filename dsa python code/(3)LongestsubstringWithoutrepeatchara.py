
def longsubstring(str):
    seen={}
    max_len = 0
    left = 0
    for index,char in enumerate(str):
        if char in seen:
            left = max(left , seen[char] +1)

        seen[char] = index

        max_len = max(max_len , index - left +1)

    return max_len



s="1R1T7"
print(longsubstring(s))
