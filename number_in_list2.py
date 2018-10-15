# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number
def string_into_int(string):
    temp=[]
    for singleElementOfString in string:
        singleElementOfString = int(singleElementOfString)
        temp.append(singleElementOfString)
    return temp
def numbers_in_lists(string):
    input_list=string_into_int(string)
    # print input_list
    input_list_lenght=len(input_list)
    # print input_list_lenght
    output_list=[]
    # print output_list
    output_list_lenght=len(output_list)
    # print output_list_lenght
    output_list_track=0
    # print output_list_track
    input_list_track=0
    # print input_list_track
    # print output_list_lenght!=input_list_lenght

    while output_list_lenght!=input_list_lenght:
        input_list_value=input_list[input_list_track]
        if output_list_lenght==0:
            output_list.append(input_list_value)
            if input_list_track!=input_list_lenght-1:
                input_list_track=input_list_track+1
                output_list_lenght=output_list_lenght+1

        else:
            print input_list[input_list_track]>=output_list[output_list_track]
            output_list.append(input_list_value)
            output_list_track=output_list_track+1
            input_list_track=input_list_track+1
            output_list_lenght=output_list_lenght+1
            # else:
            #     input_list_value=[input_list_value]
            #     output_list.append(input_list_value)
            #     output_list_track=output_list_track+1
            #     input_list_track=input_list_track+1
            #     output_list_lenght=output_list_lenght+1
    return output_list





#testcases
string = '543987'
print numbers_in_lists(string)
 # string = '543987'
 # result = [5,[4,3],9,[8,7]]
 # print repr(string), numbers_in_lists(string) == result
# string= '987654321'
# result = [9,[8,7,6,5,4,3,2,1]]
# print repr(string), numbers_in_lists(string) == result
# string = '455532123266'
# result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
# print repr(string), numbers_in_lists(string) == result
# string = '123456789'
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print repr(string), numbers_in_lists(string) == result
