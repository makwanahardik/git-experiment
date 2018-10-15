# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
# def col(lss):
#     main_temp=[]
#     for index in range(0,len(lss)):
#         temp=[]
#         for ls in lss:
#             value=ls[index]
#             temp.append(value)
#         main_temp.append(temp)
#     return main_temp


def symmetric(lss):
    cs=col(lss)
    n = len(lss)
    for i in range(0,n):
        if len(cs[i]) != n:
            return False
        else:
            if cs[i]==lss[i]:
                return True
            else:
                return False
    #
    # for cols in cs:
    #     for rows in lss:
    #         if cols==rows:
    #             return True
    #         else:
    #             return False



print symmetric([['cricket', 'football', 'tennis'], ['golf']])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

print symmetric([[1]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
