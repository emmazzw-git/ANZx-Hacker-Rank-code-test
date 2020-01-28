# Game: Distinct array
# Pre-requisite: Given an array that has 3 or more elements
# Start Game: Select three random elements, remove the smallest and largest, put back the remaining element
# Keep playing the game until there are only distinct elements left in the array
# Output the max number of elements for dictinct array

def distinctArray(array):
    # get distinct array element set
    array_element = set(array)
    occurence_map = {}
    for i in array_element:
        # count the occurence of each distinct array element 
        occurence_map[i] = array.count(i)
        
    # when number of occurrences of an array element is more than or equal to three
    for key in occurence_map:
        # maximize the number of distinct array element by reducing the number of duplicant array elements
        if occurence_map[key] >= 3 and occurence_map[key] % 2 == 1:
            occurence_map[key] = 1
        elif occurence_map[key] > 3 and occurence_map[key] % 2 == 0:
            occurence_map[key] = 2

    
    # when number of occurrence of an array element is more than or equal to two
    num_two_occurences = 0
    max_num_array = 0
    for key in occurence_map:
        if occurence_map[key] == 2:
            num_two_occurences += 1
    # a pair of array element occurrence = 2 will keep both elements in the final distinct array
    if num_two_occurences % 2 == 0:
        max_num_array = len(occurence_map.keys())
    # one array element occurrence = 2 and one array element occurrence = 1 will keep only one element in the final
    # distinct array
    else:
        max_num_array = len(occurence_map.keys()) - 1
        
    
    print('array_element', array_element)
    print('occurence_map', occurence_map)
    print('max_num_array', max_num_array)
            
    return max_num_array
    

distinctArray([2,2,3,1,4,2,1,5,5,6,7,8,6,9,2,3,9,9,7,9,9])
