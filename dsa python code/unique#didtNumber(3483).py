class Solution:
    def totalNumbers(digits):
        valid = [
    digits[i] * 100 + digits[j] * 10 + digits[k]
    for i in range(len(digits)) for j in range(len(digits)) for k in range(len(digits))
    if digits[i] != 0 and i != j and j != k and i != k
]
        valid = list(set(valid))
    
        number = 0
        for num in valid:
            if num % 2 == 0:
                number +=1
        return number