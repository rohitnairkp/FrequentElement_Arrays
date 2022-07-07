import numpy as np
from numpy import *

def get_user_input():
    # Array holding user input
    arr1 = np.array([])
    for i in range(total_elements):
        values = input('Element ➜ ')
        arr1 = append(arr1,values)
    input_array = arr1.astype(int)
    return input_array

def process_output(user_input,frequent_element):
    # Divide each element in user input array with the frequent element
    arr2 = user_input/frequent_element
    # Variable holding arr2 as list
    arr_list = list(arr2)
    output_array = []
    for j in arr_list:
        if j % 1.0 == 0:
            out = int(j)
        else:
            out = j
        output_array.append(out)
    return output_array


if __name__ == "__main__":
    # Get input from user and store in array
    total_elements = int(input("Enter the number of values you want ➜ "))
    user_input = get_user_input()
    print("User Input ➜ ",user_input)
    frequent_element = np.bincount(user_input).argmax()
    print("Frequent Element ➜ ",frequent_element)
    # Final array after all the calculations are done
    final_output = process_output(user_input,frequent_element)
    print("Output ➜",final_output)



