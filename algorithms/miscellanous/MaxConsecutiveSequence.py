'''
Q: given a list of integers L, find the maximum length of a sequenece of consecutive number
that can be formed using elements from L

Time Complexity : O(n)
[5, 2, 99, 3, 4, 1, 100]
'''


def find_maximum_length_sequence(arr):
    set_arr = frozenset(arr)

    length = 0
    for index in range(len(arr)):
        inner_length = 0
        curr_element = arr[index]
        if curr_element - 1 not in arr:
            while curr_element in set_arr:
                inner_length += 1
                curr_element += 1
            length = max(length, inner_length)
    return length


def main():
    arr = [5, 2, 99, 3, 4, 1, 100]
    print(find_maximum_length_sequence(arr))


if __name__ == "__main__":
    main()
