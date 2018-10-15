def sum_list(p):
    sum = 0
    for e in p:
        sum = sum + e
    return sum

print sum_list([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,0,0,8,67,5,5,4,3,3])

def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
   return False

print has_duplicate_element([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,0,0,8,67,5,5,4,3,3])

def mystery(p):
   i = 0
   while True:
       if i >= len(p):
           break
       if p[i] % 2:
           i = i + 2
       else:
           i = i + 1
   return i

print mystery([1,1,5])