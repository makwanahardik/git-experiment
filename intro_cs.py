# def bigger(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def smaller(a,b):
#     if a < b:
#         return a
#     else:
#         return b
#
# def biggest(a,b,c):
#     return bigger(a,bigger(b,c))
#
# def smallest(a,b,c):
#     return smaller(a,smaller(b,c))
#
# def median(a,b,c):
#     max = biggest(a,b,c)
#     min = smallest(a,b,c)

#     return (min,max)
# print (median(10,20,30))
# def find_last(string,str_string):
#
#     position=string.find(str_string)
#     return position
# print find_last("abcdefgh","i")

# def test():
#     test_cases = [
#         ((2012,1,1,2012,2,28), 58),
#         ((2012,1,1,2012,3,1), 60),
#         ((2011,6,30,2012,6,30), 366),
#         ((2011,1,1,2012,8,8), 585 ),
#         ((1900,1,1,1999,12,31), 36523)
#                   ]
#
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed", 'expected', answer, 'result', result
#         else:
#             print "Test case passed!", args, 'result', result
#
# test()

p=[1,2]
def proc1(p):
    q=[]
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())
    print p
print p
proc1(p)
