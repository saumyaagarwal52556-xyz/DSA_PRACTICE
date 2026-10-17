def repeatedPattern(str):
    temp = str +str
    temp = temp[1:-1]
    if str in temp:
        return True
    else:
        return False


#problem time complexity

    # temp = list(str)
    # main = list(str)

    # for _ in range(len(str) -1):
    #     temp.append(temp[0])
    #     temp.pop(0)
    #     if(temp == main):
    #         return True

    # return False


str="aba"
print(repeatedPattern(str))