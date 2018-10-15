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


def check_sudoku(lss):
    uel = unique_element(lss)
    for ls in lss:
        for ue in uel:
            if ue in ls:
                for j in range(len(lss)):
                    for i in range(len(lss)):
                        print lss[j][i]
                # for i in range(len(lss)):
                #     for i in range(len(lss)):
                #         if ue in lss[i]:
                #             pass



            else:
                return False
    #
    # for j in range(len(lss)):
    #     # for i in range(len(lss)):
    #         print lss[j]

    return True




print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
