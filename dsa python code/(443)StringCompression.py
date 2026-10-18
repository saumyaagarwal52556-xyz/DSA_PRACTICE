def compression(arr):
    read = 0
    write =0


    while read<len(arr):
        current = arr[read]
        count = 0

        while( read < len(arr) and current == arr[read]):
            read += 1
            count += 1

        arr[write] = current
        write += 1

        if count>1:
            for digit in str(count):
                arr[write] = digit
                write += 1

    arr[:] = arr[:write]
    return arr



    # temp={}
    
    # for char in str:
    #     if char in temp:
    #         temp[char] +=1
    #     else:
    #         temp[char] =1

    # print(temp)
    # result =[] 
    # for key,value in temp.items():
    #     if temp[key] ==1:
    #         result.append(key)
    #     else:
    #         result.append(key)
    #         while(value !=0):
    #             rem = value %10
    #             value //=10
    #             result.append(rem)

    # print(result)
    # str[:] = result
    # return str
            

chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compression(chars))