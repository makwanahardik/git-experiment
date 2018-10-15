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

incorrect6=[[2,2,2], [2,2,2], [2,2,2]]

incorrect7=[[1,2,3,4], [2,4,1,3], [3,1,4,2], [4,3,2,1]]

incorrect8=[
            [1,2,4],
            [2,4,1],
            [4,1,2]
            ]
def unique_element(ls):
    unique=[]
    for l in ls:

        for e in l:
            if type(e) is int and e!=0:
                if e not in unique:
                    unique.append(e)
                # else:
                #     return False
            else:
                return False
    if len(unique)==len(ls):
        return unique
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


def row(lss):
    main_temp=[]
    # temp=[]
    for ls in lss:
        main_temp.append(ls)
    return main_temp

def check_sudoku(lss):
    rows=row(lss)              #rows
    cols=col(lss)             # columns
    uel=unique_element(lss)  # unique element list
    if uel!=False:
        for ue in uel:
            for rs in rows:
                if ue in rs:
                    continue
                else:
                    return False
            for cs in cols:
                if ue in cs:
                    continue
                else:
                    return False
    else:
        return False
    return True


print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
# >>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect5)
#>>> False
print check_sudoku(incorrect4)
# >>>False

print check_sudoku(incorrect7)
# >>>True

print check_sudoku(incorrect6)
#>>>False

print check_sudoku(incorrect8)
#>>>
