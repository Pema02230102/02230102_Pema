    #====================
    #CREATE INDEX TABLE
    #====================

def create_index_table(arr, block_size):
    index_table = []

    # Loop through list in steps of block_size
    for i in range(0, len(arr), block_size):
        # Store first element of block and its index
        index_table.append((arr[i], i))

    print("Index table created:")
    for value, index in index_table:
        print(value, "->", index)

    return index_table


# Example usage
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

index_table = create_index_table(arr, block_size)