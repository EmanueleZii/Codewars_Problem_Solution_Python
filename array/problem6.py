'''
<summary>
    Given an array of integers your solution should find the smallest integer.

    For example:

        Given [34, 15, 88, 2] your solution will return 2
        Given [34, -345, -1, 100] your solution will return -345

    You can assume, for the purpose of this kata, that the supplied array will not be empty.
Level: 8kyu
</summary>
'''


def find_smallest_int(arr):
    min_arr = min(arr)
    return min_arr

def main():
    arr = [34, 15, 88, 2]
    print(find_smallest_int(arr))

if __name__ == '__main__':
    main()