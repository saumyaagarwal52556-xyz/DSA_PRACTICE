def isPalindrome(s):
    new = "".join(char for char in s if char.isalnum()).lower()

    return new == new[::-1]