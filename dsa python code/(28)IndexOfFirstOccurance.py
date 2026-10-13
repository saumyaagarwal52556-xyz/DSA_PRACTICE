def FirstOccurance(main , sub):
    result = main.find(sub)
    return result
    # found = []
    # index = 0
    # for i in range(len(main)):
        
    #     if( index <len(sub) and main[i] == sub[index] ):
    #         index +=1
    #         found.append(i)
    #     else:
    #         index = 0
    #         if(found):
    #             found.pop(0)
    
    # return found[0] if len(found)==len(sub) else -1


haystack = "mississippi"
needle ="issip"
print(FirstOccurance(haystack , needle))