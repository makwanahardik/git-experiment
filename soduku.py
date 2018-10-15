correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def unique_element(ls):
    unique=[]
    for l in ls:
        for e in l:
            if e not in unique:
                unique.append(e)
    return unique

# def count_element(ls):
#     uel=unique_element(ls)
#     for ue in uel:
#         for l in ls:
#             if ue in l:
#                 pass
#             else:
#                 return False
#     return True

def check_sudoku(ls):
    uel=unique_element(ls)
    for ue in uel:
        for j in len(ls):
            for i in range(len(ls)):

# print check_sudoku(correct)
# print check_sudoku(incorrect)
