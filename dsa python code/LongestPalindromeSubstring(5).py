def palindrome(str):
    
    def expand(s , left , right):
        max_len = 0
        substring =''
        while(left >=0 and right < len(str) and str[left] == str[right]):
            if(right - left +1 > max_len):
                max_len = right - left + 1
                substring= s[ left : right +1]
            left -=1
            right +=1

        return substring

    result =""

    for i in range(len(str)):
        odd = expand(s , i , i)
        even = expand(s , i , i+1)

        if len(odd) > len(result):
            result = odd

        if len(even) > len(result):
            result = even

    return result


        

s="cbbd"
print(palindrome(s))
    

        