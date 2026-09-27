def logestSubPalindrome(s):
    max_len = 0
    start = 0

    for i in range(len(s)):

        for left,right in [(i,i) , (i,i+1)]:

            while left >= 0 and right < len(s) and s[left ]== s[right]:
                current_length = right - left + 1

                if current_length > max_len:
                    max_len = current_length
                    start = left

                left -= 1
                right += 1

        

    return s[start : start + max_len]


s="babad"
print(logestSubPalindrome(s))