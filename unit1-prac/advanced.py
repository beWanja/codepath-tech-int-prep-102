def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def final_value_after_operations(operations):
    tigger = 1
    for i in range(len(operations)):
        if operations[i] == 'flouncy' or operations[i] == 'bouncy':
            tigger += 1
        elif operations[i] == 'trouncy' or operations[i] == 'pouncy':
            tigger -= 1
    return tigger

"""
Given an array nums with n integers, write a function non_decreasing() 
that checks if nums could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""
def non_decreasing(nums):
    for i in range(len(nums) -1):
        if nums[i] > nums[i+1]:
            return False
    return True

def main():

    print("----TARGET----")
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

    print("----OPERATIONS----")

    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

    print("----NONDECREASING----")

    nums = [4, 2, 3, 5, 0, 6]
    print(non_decreasing(nums)) # False

    nums = [111, 5, 2, 1]
    print(non_decreasing(nums)) # True



if __name__ == "__main__":
    main()