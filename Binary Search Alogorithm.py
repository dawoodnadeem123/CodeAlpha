def binary_search(A, key):
    A = sorted(A)  # Ensure the list is sorted for binary search
    f_index = 0
    l_index = len(A) - 1
    flag = 0

    while f_index <= l_index and flag == 0:
        mid = (f_index + l_index) // 2

        if A[mid] == key:
            flag = 1
        elif key < A[mid]:
            l_index = mid - 1
        else:
            f_index = mid + 1

    return flag

# Usage example:
my_list = [3, 7, 10, 15, 24, 56, 65]
search_key = 56

result = binary_search(my_list, search_key)#here i am  making a variable, ie result so that i could save the output which will come from top from the binary search function we have made
#and then we are calling the dunction binary search function and passing the list ie mylist and search key asits argumwents they will go ion the top in the ninary search function and rest of the code will dp its processing and the if flag becaomes one means the okect ie the search key have been found so the vlaueof flag will be returned as 1
#and if the value of flag has been returned as 1 (means the value have been found by the binary search algorithm ) so it will gp to the if statement ie 1==1 true condition and the body of if statement will run telling you that the search key have been found in your given list.

if result == 1:
    print(search_key," found in the list.")
else:
    print(search_key," not found in the list.")
