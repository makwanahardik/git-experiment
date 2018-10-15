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


def col(lss):
    main_temp=[]
    for index in range(0,len(lss)):
        temp=[]
        for ls in lss:
            value=ls[index]
            temp.append(value)
        main_temp.append(temp)
    return main_temp

def check_sudoku(lss):
    n=len(lss)
    cols=col(lss)             # columns
    # print n

    for l in lss:
        # print l
        for value in range(1,n+1):
            # print value
            if value in l:
                for cs in cols:
                    if value in cs:
                        continue
                    else:
                        return False
            else:
                return False
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
#>>> Fals
