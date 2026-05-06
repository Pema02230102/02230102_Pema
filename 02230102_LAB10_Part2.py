#==================================
#PART 2;RADIX SORT IMPLEMENTATION 
#==================================

class RadixSort:

    # Counting Sort used as a subroutine (for a specific digit)
    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n          # Output array
        count = [0] * 10         # Digits 0–9

        # Step 1: Count occurrences of digits
        for i in range(n):
            digit = (arr[i] // exp) % 10
            count[digit] += 1

        # Step 2: Convert to cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Step 3: Build output array (right to left → stable)
        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        # Step 4: Copy back to original array
        for i in range(n):
            arr[i] = output[i]

    # Main Radix Sort function
    def sort(self, arr):
        # Step 1: Find maximum number
        max_val = max(arr)

        exp = 1  # Represents 1s, 10s, 100s, ...

        # Step 2: Process each digit
        while max_val // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10

    # Display function
    def display(self, arr):
        print("Sorted array:", arr)


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]

rs = RadixSort()
rs.sort(arr)
rs.display(arr)