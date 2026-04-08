#=========================================
#PART 1: SEQUENTIAL SEARCH IMPLEMENTATION
#=========================================

# Function for Sequential Search
def sequential_search(arr, target):
    # Count number of comparisons
    comparisons = 0

    # Traverse the list one by one
    for i in range(len(arr)):
        comparisons += 1  # Increment comparison count

        # Check if current element matches target
        if arr[i] == target:
            return i, comparisons  # Return index and comparisons

    # If not found
    return -1, comparisons


# ==========================
# MAIN PROGRAM (TESTING)
# ==========================

arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

print("List:", arr)
print(f"Searching for {target} using Sequential Search")

index, comp = sequential_search(arr, target)

if index != -1:
    print("Found at index", index)
else:
    print("Element not found")

print("Number of comparisons:", comp)