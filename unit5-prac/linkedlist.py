class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next




# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

"""
Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.
"""
kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")


saharah.next = isabelle
harriet.next = saharah
kk_slider.next = harriet

isabelle = None 
saharah = None
harriet = None

print_linked_list(kk_slider)