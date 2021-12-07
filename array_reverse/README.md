## Reverse an Array - 12/06/2021

Write a function which takes a list an argument. Without utilizing any of the build-in methods available to your language, return a list with elements in reversed order.

## Whiteboard Process

![Reverse a list](array_reverse.png)

## Approach & Efficiency

- Approach 1: create a reversed list based on input list and return it
  - Algorithm:
    - Create an empty list: reversed_list
    - Iterate backwards through the input list
    - Each iteration, append current element to reversed_list
    - Return reversed_list upon completion of all iterations
  - Efficiency:
    - Time complexity: O(n)
- Approach 2: reverse input list in-place and return it
  - Algorithm:
    - Find midpoint index based on input list length
    - Iterate over input list from first element to midpoint element
    - Each iteration, swap current element with element at index (leng(input_list) - 1 - current index)
    - retun input list upon completion of all iterations
  - Efficiency:
    - Time complexity: O(N). Performance-wise, this algorithm is better than first algorithm because it only iterates over half of the input list.
