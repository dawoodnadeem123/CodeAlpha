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

result = binary_search(my_list, search_key)

if result == 1:
    print(search_key," found in the list.")
else:
    print(search_key," not found in the list.")
