
def CommonPrefix(strs):
    result =strs[0]

    for s in strs[1:]:
        # here we are checking does s contain result if not reduce the result

        while not s.startswith(result):
            result = result[:-1]  #remove the last letter
    return result
    


strs = ["flower","flow","flight"]
print(CommonPrefix(strs))