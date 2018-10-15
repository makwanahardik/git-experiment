# Question 8: Longest Repetition
# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l):
    Gking = None
    Gscore = 0
    previou_seen=None
    previou_seen_score=0
    for data in l: 
        if previou_seen==None:
            previou_seen=data
            previou_seen_score=1
        elif previou_seen==data:
            previou_seen_score=previou_seen_score+1
        else:
            previou_seen=data
            previou_seen_score=1

        if Gscore < previou_seen_score:
            Gking=previou_seen
            Gscore=previou_seen_score

        # print(data)
        # print(previou_seen, previou_seen_score)
        # print(Gking, Gscore)
    # print(Gking, Gscore)
    return Gking
        
    
    


#For example,
print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition([1])


print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# # 1

print longest_repetition([])
# # None

