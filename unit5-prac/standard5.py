class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    """
    If new_catchphrase is valid, it should update the villager's 
    catchphrase attribute to have value new_catchphrase and print "Catchphrase updated"
    Valid catchphrases are less than 20 characters in length. 
    They must all contain only alphabetic and whitespace characters.
    """
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) >= 20 or not new_catchphrase.replace(" ", "").isalpha():
            print("Invalid catchphrase")
        else:
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")

    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"]:
            self.furniture.append(item_name)
    """
    The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" 
    for however many unique items exist in the villager's furniture list
    If the player has no items, the function should print "Inventory empty".
    """
    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty!")
        else:
            freq_map = {}
            for item in self.furniture:
                freq_map[item] = freq_map.setdefault(item, 0) + 1

            print(", ".join(f"{key}: {value}" for key, value in freq_map.items()))



def main():
    apollo = Villager("Apollo", "Eagle", "pah")
    bones = Villager("Bones", "Dog", "yip yip")
    alice = Villager("Alice", "Koala", "guvnor")


    print("---P1---")
    print(apollo.name)  
    print(apollo.species)  
    print(apollo.catchphrase) 
    print(apollo.furniture) 

    print("---P2---")
    print(bones.greet_player("Beauttah"))

    print("---P3---")
    alice.set_catchphrase("sweet dreams")
    print(alice.catchphrase)
    alice.set_catchphrase("#?!")
    print(alice.catchphrase)

    print("---P4---")
    alice.add_item("acoustic guitar")
    print(alice.furniture)

    alice.add_item("cacao tree")
    print(alice.furniture)

    alice.add_item("nintendo switch")
    print(alice.furniture)
    
    print("---P5---")
    bones.print_inventory()
    alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
    print(alice.furniture)

    return None

if __name__ == "__main__":
    main()