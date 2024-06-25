# To sort an array of 0, 1 and 2's only
# Example :
# Input  : [2,1,0,1,0,1]
# Output  :[0,0,1,1,1,2]
# O(n) time, O(1) Space

input_array = [2, 1, 0, 2, 0, 1, 0, 1]


def sort_dfa(input):
    zero_index = 0
    one_index = 0
    two_index = len(input) - 1

    print(input)

    '''
    Algorithm  : 
    1. Using 3 pointers for 0's, 1's and 2's. Keep moving 1's pointer 
    2. Initialize 0's and 1's index to 0, 2's index to last element index
    3. Iterate over the array
        3a. If element is 0, swap values between 0's and 1's index. increment 0's index, increment 1's index  
        3b. if element is 1, no value swap. increment 1's index and move to the next element
        3c. if element is 2, swap values between 1's and 2's index. decrement 2's index 
    
    '''
    while one_index <= two_index:

        print(zero_index, one_index, two_index, input)

        val = input[one_index]
        if val == 0:
            temp = input[zero_index]
            input[zero_index] = input[one_index]
            input[one_index] = temp
            zero_index = zero_index + 1
            one_index = one_index + 1

        elif val == 1:
            one_index = one_index + 1

        elif val == 2:
            temp = input[one_index]
            input[one_index] = input[two_index]
            input[two_index] = temp
            two_index = two_index - 1

        else:
            raise Exception("Unsupported value:", val)
    return input


output = sort_dfa(input_array)
print(output)
# output = [0, 0, 1, 1, 1, 2]
expected_output = [0, 0, 0, 1, 1, 1, 2, 2]

assert output == expected_output
