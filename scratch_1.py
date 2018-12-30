
def longest_consecutive(array):

    array.sort()
    actual_sequence = []
    last_sequence = []

    index = 1

    while index < len(array) :
        if array[index]-1  == array[index-1]:
            actual_sequence.append(array[index-1])

        else:
            actual_sequence.append(array[index - 1])
            if len(actual_sequence) > len(last_sequence):
                last_sequence = actual_sequence[:]
                actual_sequence = []

        index += 1

    if len(actual_sequence) > len(last_sequence):
        print(actual_sequence)
    else:
        print(last_sequence)




array = [2, 4, 9,45, 6,12,13, 5, 8,1, 3, 0,10,11]
array2 =[2,1,6,4,9,3]

longest_consecutive(array)
