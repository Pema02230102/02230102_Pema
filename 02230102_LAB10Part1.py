#====================================
#PART 1;COUNTING SORT IMPLEMENTATION
#====================================

def counting_sort(arr):
    # Step 1: Find maximum value
    max_val = max(arr)

    # Step 2: Create count array
    count = [0] * (max_val + 1)

    # Step 3: Count occurrences (handles duplicates)
    for num in arr:
        count[num] += 1

    # Step 4: Reconstruct sorted array
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


# Input array
arr = [4, 2, 2, 8, 3, 3, 1]

# Sort and display output
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)