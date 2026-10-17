def countLastword(str):
    max =0
    count =0

    for i in range(len(str)):
        if str[i] != " ":
            count +=1
            max = count

        elif str[i] == " " and i != len(str):
            
            count =0

    return max

str="   fly me   to   the moon   "
print(countLastword(str))