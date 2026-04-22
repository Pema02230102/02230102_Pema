#========================================
# SELECTION SORT WITH COMPARISONS & SWAPS
#========================================

def selection_sort(arr):
    n = len(arr)
    comparisons = 0  # To count comparisons
    swaps = 0        # To count swaps

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1  # Count comparison
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1  # Count swap

        print(f"Pass {i+1}:", arr)

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


# Example usage
arr = [29, 10, 14, 37, 13]
selection_sort(arr)