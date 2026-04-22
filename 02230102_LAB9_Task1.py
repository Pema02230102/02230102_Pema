#===============
# SELECTION SORT
#===============

# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)

    print("Original list:", arr)

    # Loop through each element of the list
    for i in range(n - 1):
        min_index = i  # Assume current index is minimum

        # Find the smallest element in remaining unsorted list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min index

        # Swap the found minimum element with first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print list after each pass
        print(f"Pass {i+1}:", arr)

    print("Sorted list:", arr)


# Example usage
arr = [29, 10, 14, 37, 13]
selection_sort(arr)