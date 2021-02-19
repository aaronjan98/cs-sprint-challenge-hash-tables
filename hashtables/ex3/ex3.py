inter_table = {}
count = 0

def intersection(arrays):
    # lst3 = [value for value in arrays[0] if value in arrays[1]] 
    first_arr = arrays[0]
    inter_table = {first_arr[i]: False for i in range(len(first_arr))}
    # loop through the list of lists
    for array in arrays[1:]:
        # loop through every integer in each list
        for num in array:
            # if num is an intersection set it's value to True
            if num in inter_table.keys():
                inter_table.update({num: True})
        replace_table = {}
        # erase keys in inter_table that have values of False
        for key, value in inter_table.items():
            if value == True:
                replace_table.update({key: False})
        inter_table = replace_table
    inter_table = list(inter_table)
            
    return inter_table


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
