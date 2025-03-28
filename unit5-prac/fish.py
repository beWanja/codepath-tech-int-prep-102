class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next


"""
"Write a function catch_fish() that accepts the head of a list. The function should:

Print the name of the fish in the head node using the format "I caught a <fish name>!".
Remove the first node in the list.
The function should return the new head of the list. If the list is empty, 
print "Aw! Better luck next time!" and return None.
"""
def catch_fish(head):
    current = head
    if current:
        print(f"I caught a {current.fish_name}!")
        current = current.next
        head = None
        return current
    elif current is None:
        print("Aw! Better luck next time!")
        return None


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next



fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
fish_list = catch_fish(fish_list)
print_linked_list(fish_list)
fish_list = catch_fish(fish_list)
print_linked_list(fish_list)
# print(catch_fish(empty_list))