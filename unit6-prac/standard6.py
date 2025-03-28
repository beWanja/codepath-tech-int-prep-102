# Question 1

# class SongNode:
# 	def __init__(self, song, next=None):
# 		self.song = song
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
		
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# bad_romance = SongNode("Bad Romance", None)
# party_rock_anthem = SongNode("Party Rock Athem", bad_romance)
# uptown = SongNode("Uptown Funk", party_rock_anthem)

# print_linked_list(uptown)

# # Uptown Funk -> Party Rock Anthem -> Bad Romance

# Question 2
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# def get_artist_frequency(playlist):
    
#     freq = {}
    
#     curr_song = playlist
    
#     while curr_song:
#         if curr_song.artist in freq:
#             freq[curr_song.artist] += 1
#         else:
#             freq[curr_song.artist] = 1
#         curr_song = curr_song.next
        
#     return freq


# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

# { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}

# Question 3

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
# def remove_song(playlist_head, song):
#     if not playlist_head:
#         return None
#     if playlist_head.song == song:
#         return playlist_head.next

#     current = playlist_head
#     while current.next:
#         if current.next.song == song:
#             current.next = current.next.next  
#             return playlist_head 
#         current = current.next

#     return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))
# # ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')
# print("__")
# playlist = SongNode("SOS", "ABBA")

# print_linked_list(remove_song(playlist, "SOS"))
# # Return None
# print("test ")
# playlist = None

# print_linked_list(remove_song(playlist, "SOS"))
# # Return None

# print("__")

# playlist = SongNode("SOS", "ABBA", SongNode("Dreams", "Fleetwood Mac"))
# print_linked_list(remove_song(playlist, "SOS"))
# # Return Dreams


# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "SOS"))

# playlist = remove_song(playlist, "SOS")
# print_linked_list(remove_song(playlist, "Lovely Day"))

# Return Simple -> Dreams

# Question 4

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# def on_repeat(playlist_head):
#     slow = playlist_head
#     fast = playlist_head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False


# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

# Question 5:

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
        if slow == fast:
            meeting_point = slow
            cnt = 1
            curr = slow
            
            while curr != slow:
                cnt += 1
                curr = curr.next
                
            return cnt
    return None




song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))