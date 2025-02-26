"""
Function takes list of words and returns a frequency map of each word with the word as key and frequency as value
"""
def freq_map(list):
    my_map = {list[0]: 1}

    for i in range(1, len(list)):
        if list[i] in my_map:
            my_map[list[i]] += 1
        else:
            my_map[list[i]] = 1
    return my_map


"""
Given two lists of strings artists and set_times of length n, 
write a function lineup() that maps each artist to their set time.
An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).
"""
def lineup(artists, set_times):
    my_map = {}
    for i in range(len(artists)):
        my_map[artists[i]] = set_times[i]
    return my_map

"""
Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule
mapping artist's names to dictionaries containing the day, time, and stage they are playing on. 
Return the dictionary containing the information about the given artist.
If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.
"""
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule.get(artist)
    else:
        return {"message": "Artist not found"}

"""
A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.
"""
def total_sales(ticket_sales):
    total = 0
    for sales in ticket_sales.values():
        total += sales
    return total

"""
Implement a function identify_conflicts() that accepts two dictionaries 
venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. 
Return a dictionary containing the key-value pairs that are the same in each schedule.
"""
def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}
    for artist, time in venue1_schedule.items():
        if artist in venue2_schedule and time == venue2_schedule.get(artist):
            result[artist] = time
    return result


"""
Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.
"""
#----PROBLEM 5----
def best_set(votes):
    artist_vote = {}  
    for artist in votes.values():
        if artist in artist_vote:
            artist_vote[artist] += 1
        else:
            artist_vote[artist] = 1
    
    max_vote = max(artist_vote.values())
    # print(artist_vote) # sanity check
    for artist, vote in artist_vote.items():
        if vote == max_vote:
            return {artist:vote}


# ----PROBLEM 6----
"""
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.
Return the combined audience size of all performances in audiences with the maximum audience size.
The audience size of a performance is the number of people who attended that performance.
"""
def max_audience_performances(audiences):
    aud_map = {}
    for i in range(len(audiences)):
        if audiences[i] in aud_map:
            aud_map[audiences[i]] += 1
        else:
            aud_map[audiences[i]] = 1

    max_audience = max(aud_map.keys())
    for aud_size, freq in aud_map.items():
        if aud_size == max_audience:
            return aud_size*freq


        


def main():
    my_list = ["trouncy", "flouncy", "flouncy", "bouncy", "doc", "flouncy"]
    print(freq_map(my_list))

    print("----ARTIST-MAP----")
    artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
    set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
    artists2 = []
    set_times2 = []

    print(lineup(artists1, set_times1))
    print(lineup(artists2, set_times2))

    print("----PROBLEM 2----")
    festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
    }

    print(get_artist_info("Blood Orange", festival_schedule)) 
    print(get_artist_info("Taylor Swift", festival_schedule)) 

    print("----PROBLEM 3----")
    ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
    print(total_sales(ticket_sales))

    print("----PROBLEM 4----")
    venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
        "Bruce Springsteen": "6:00 PM"
    }
    venue2_schedule = {
        "Stromae": "9:00 PM",
        "Janelle Monáe": "10:30 PM",
        "HARDY": "7:00 PM",
        "Wizkid": "6:00 PM"
    }
    print(identify_conflicts(venue1_schedule, venue2_schedule))

    print("----PROBLEM 5----")
    votes1 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA",
        1239: "SZA"
    }
    votes2 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA"
    }

    print(best_set(votes1))
    print(best_set(votes2))

    print("----PROBLEM 6----")
    audiences1 = [100, 200, 200, 150, 100, 250]
    audiences2 = [120, 180, 220, 150, 220]

    print(max_audience_performances(audiences1))
    print(max_audience_performances(audiences2))



if __name__ == "__main__":
    main()