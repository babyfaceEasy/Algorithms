'''
Q: reverse given array in place.

Time complexity: O(n)
Space complexity: O(1)

E.g :
Input = [0, 1, 2, 3, 4, 5, 6, 7]
Output = [7, 6, 5, 4, 3, 2, 1, 0]
'''
import types


def reverseInPlace(arr):
    if type(arr) != list:
        return []

    front_index = 0
    back_index = len(arr) - 1

    while front_index < back_index:
        # this can be replaced with a swap function e.g swap (arr, front_index, back_index)
        temp = arr[front_index]
        arr[front_index] = arr[back_index]
        arr[back_index] = temp
        front_index += 1
        back_index -= 1
    # you are free to return the passed array or just print it after the function call
    return arr


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print(reverseInPlace(arr))


if __name__ == "__main__":
    main()
