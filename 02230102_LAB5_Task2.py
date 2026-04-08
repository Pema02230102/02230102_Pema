#======================================
#PART 2: BINARY SEARCH IMPLEMENTATION
#======================================

# Iterative Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Recursive Binary Search
def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons

    mid = (low + high) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# ==========================
# MAIN PROGRAM (TESTING)
# ==========================

arr = [12, 23, 34, 45, 56, 67, 89]  # Sorted list required
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search")

index, comp = binary_search(arr, target)

if index != -1:
    print("Found at index", index)
else:
    print("Element not found")

print("Number of comparisons:", comp)