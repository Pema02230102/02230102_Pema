        #===============
        # Key NOT FOUND
        #===============

def create_index_table(arr, block_size):
    index_table = []
    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
    return index_table


def indexed_search(arr, index_table, key):
    print("Search key:", key)

    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]

            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            break

    print("Index range found:")
    print(f"Searching from index {imin} to index {imax}:")

    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1


# Main
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = create_index_table(arr, 3)

indexed_search(arr, index_table, 43)