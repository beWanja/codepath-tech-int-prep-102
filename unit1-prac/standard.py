'''
Implement a function get_item() that accepts a 0-indexed list items and a 
non-negative integer x and returns the element at index x in items. 
If x is not a valid index of items, return None.
'''
def get_item(items, x):
    length = len(items) # if x in range(len(items))
    if x >= length:
        return None
    else:
        return items[x]

"""
Missing docstring here!!
"""
def nanana_batman(x):
    if x < 0:
        raise ValueError("Input must be positive in range 0-MAX INT") 
    if x == 0:
        return "batman!"
    else:
        result = ""
        for i in range(x):
            result += "na"
        result += " batman!"
    return result

"""
Implement a function count_evens() that accepts a 
list of strings lst as a parameter. 
The function should return the number of strings 
with an even length in the list.
"""

def count_evens(lst):
    count = 0
    for word in lst:
        if len(word) % 2 == 0:
            count += 1
    return count

"""

Write a function remove_name() to keep Batman's secret identity hidden. 
The function accepts a list of names people and a string secret_identity and 
should return the list with any instances of secret_identity removed. 
The list must be modified in place; 
you may not create any new lists as part of your solution. 
Relative order of the remaining elements must be maintained.
"""
def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people


"""
Given a non-negative integer n, write a function count_digits()
that returns the number of digits in n. 
You may not cast n to a string.
"""
def count_digits(n):
    digit = 0
    if n == 0: # because n is nonnegative
        return 1
    while n > 0:
        digit += 1
        n //= 10
    return digit 


"""
Write a function move_zeroes that accepts an integer array nums
 and returns a new list with all 0s moved to the end of list. 
 The relative order of the non-zero elements in the original 
 list should be maintained.
"""
def move_zeroes(lst):
    non_zero_list = [num for num in lst if num != 0]
    zero_counter = len(lst) - len(non_zero_list)
    return non_zero_list + [0] * zero_counter

"""
Given a string s, reverse only all the vowels in 
the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they 
can appear in both lower and upper cases and more than once.
"""
def reverse_vowels(s):
    vowels = "aeiouAEIOU"

    vowels_in_str = [vowel for vowel in s if vowel in vowels] 
    # print(vowels_in_str) # quick check
    s_list = list(s)

    for index, char in enumerate(s):
        if char in vowels:
           s_list[index] = vowels_in_str.pop()
    return "".join(s_list)

"""
Write a function highest_altitude() that accepts an integer array gain of length n
where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.
"""
def highest_altitude(gain):
    altitude = 0
    highest_point = 0

    for val in gain:
        altitude += val
        highest_point = max(altitude,highest_point)

    return highest_point

"""
Given a 0-indexed integer array nums, 
write a function left_right_difference that returns a 0-indexed integer array answer where:
    len(answer) == len(nums)
    answer[i] = left_sum[i] - right_sum[i]
Where:
    left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
    right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0
"""
def left_right_difference(nums):
    pass  


"""
Write a function common_elements() that takes in two lists lst1 and lst2 and 
returns a list of the elements that are common to both lists.
"""
def common_elements(lst1, lst2):
    pass



def main():
    print("-----GET ITEM-----")
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    print(get_item(items, x))
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    print(get_item(items, x))

    print("-----NANANA BATMAN-----")
    print(nanana_batman(0)) # batman!
    print(nanana_batman(5)) # nanananana batman!
    # print(nanana_batman(-5)) # raise error

    print("-----EVENS-----")
    lst = ["na", "nana", "nanana", "batman", "!"]
    print(count_evens(lst))
    lst = ["the", "joker", "robin"]
    print(count_evens(lst))
    lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
    print(count_evens(lst))

    print("-----REMOVE NAME -----")
    people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
    secret_identity = 'Bruce Wayne'
    print(remove_name(people, secret_identity))

    print("-----DIGITS-----")
    n = 964
    print(count_digits(n))
    n = 0
    print(count_digits(n))
    
    print("-----VOWELS-----")
    print(reverse_vowels("value"))
    print(reverse_vowels("robin"))
    print(reverse_vowels("BATgirl"))
    print(reverse_vowels("batman"))

    print("-----VANTAGE POINT-----")
    gain = [-5, 1, 5, 0, -7]
    print(highest_altitude(gain)) # 1
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(highest_altitude(gain)) # 0

    print("-----SUM DIFFERENCES-----")


if __name__ == "__main__":
    main()

