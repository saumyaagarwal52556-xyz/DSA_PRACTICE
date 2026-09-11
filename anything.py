def abc(str):
    result =()
    curr=()

    for i in range(len(str)):
        curr += (str[i],)
        if str[i] == str[-(i+1)]:
            result += (str[i],)

        
    return result

str = "babagdd"
print(abc(str))