def length_list_fun(input_list):
    length_list=[]
    if input_list==[]:
        return True
    for single_list in input_list:
        size_single_list=len(single_list)
        length_list.append(size_single_list)
    max_size_single_list=max(length_list)
    min_size_single_list=min(length_list)
    if min_size_single_list==max_size_single_list:
        return True
    else:
        return False

def col(lss):
    main_temp=[]
    for index in range(0,len(lss)):
        temp=[]
        for ls in lss:
            value=ls[index]
            temp.append(value)
        main_temp.append(temp)
    return main_temp

def symmetric(input_list):
    if length_list_fun(input_list) or len(input_list) ==0:
        cs=col(input_list)
        n = len(input_list)
        for i in range(0,n):
            if len(cs[i]) != n:
                return False
            else:
                if cs[i]==input_list[i]:
                    continue
                else:
                    return False
    else:
        return False
    return True



# input_list=[['cricket', 'football', 'tennis'], ['golf']]
# print symmetric(input_list)
# print symmetric([[1]])
# print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
# #>>> True
#
# print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
# #>>> False
print symmetric([])
