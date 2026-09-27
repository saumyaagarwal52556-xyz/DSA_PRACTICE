
def isValid(s):
    bracket = {")" :"(" , "}":"{" ,"]":"[" }
    result = []

    for char in s:
        if char in bracket:
            top_element = result.pop() if result else "#"

            if top_element != bracket[char]:
                return False
        else:
            result.append(char)
    return len(result) == 0
        