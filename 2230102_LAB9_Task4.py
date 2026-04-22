        #===================
        # INDEXED SEARCH
        #===================

def indexed_search(arr, index_table, key):
    print("\nSearch key:", key)

    imin = 0
    imax = 0

    # Step 1: Find range using index table
    for i in range(len(index_table)):
        # If it's the last block or key is less than next block value
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]  # Start index
            # End index is either next block start -1 or last index
            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            break

    print("Index range found:")
    print(f"{arr[imin]} <= {key} < {arr[imax+1] if imax+1 < len(arr) else 'end'}")

    print(f"Searching from index {imin} to index {imax}:")

    # Step 2: Sequential search in range
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1


# Example usage
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]

indexed_search(arr, index_table, 45)