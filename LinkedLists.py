# Instantiate song class as nodes, think of it as each railing in
class Song:
    def __init__(self, value, next_song=None, prev_song=None):
        self.value = value
        self.next_song = next_song
        self.prev_song = prev_song

    # The following methods should not be indented under __init__
    def set_next_song(self, next_song):
        self.next_song = next_song
    
    def get_next_song(self):
        return self.next_song
    
    def set_prev_song(self, prev_song):
        self.prev_song = prev_song
    
    def get_prev_song(self):
        return self.prev_song
    
    def get_value(self):
        return self.value


# Create Playlist class that hosts all of the songs, think of it as the train tracks
class Playlist:
    def __init__(self):
        self.head_song = None
        self.tail_song = None
        

    # Add Song to head (start) of playlist
    def add_to_head(self, new_value):
        new_head = Song(new_value)
        current_head = self.head_song

        # Checks if current head exists, and replaces pointers with new head
        if current_head != None:
            current_head.set_prev_song(new_head)
            new_head.set_next_song(current_head)
        
        self.head_song = new_head # Reassigns head song

        # Reassigns tail if its also head (only 1 song)
        if self.tail_song == None:
            self.tail_song = new_head


    # Add Song to tail (end) of playlist
    def add_to_tail(self, new_value):
        new_tail = Song(new_value)
        current_tail = self.tail_song

        # Checks if current tail exists, and replaces pointers with new tail
        if current_tail != None:
            current_tail.set_next_song(new_tail)
            new_tail.set_prev_song(current_tail)
        
        self.tail_song = new_tail # Reassigns tail song

        # Reassigns head if its also tail (only 1 song)
        if self.head_song == None:
            self.head_song = new_tail

    
    # Remove the head of the playlist
    def remove_head(self):
        removed_head = self.head_song

        # If no head
        if removed_head == None:
            return None
        
        self.head_song = removed_head.get_next_song() # Reassign Head

        # Switch pointers of next head song, essentially 'dissapearing' the orgiinal head song
        if self.head_song != None: 
            self.head_song.set_prev_song(None)

        # If head and tail are the same, runs the tail script to also remove the tail
        if removed_head == self.tail_song:
            self.remove_tail()

        return removed_head.get_value()

    # Remove the tail of the playlist
    def remove_tail(self):
        removed_tail = self.tail_song

        # If no tail
        if removed_tail == None:
            return None
        
        self.tail_song = removed_tail.get_prev_song() # Reassign tail

        # Switch pointers of prev tail song, essentially 'dissapearing' the orgiinal tail song
        if self.tail_song != None: 
            self.tail_song.set_next_song(None)

        # If tail and head are the same, runs the head script to also remove the head
        if removed_tail == self.head_song:
            self.removed_head()

        return removed_tail.get_value()


    # Remove song by specific value (song name)
    def remove_by_value(self, value_to_remove):
        song_to_remove = None
        rotated_song = self.head_song

        # Iterate through playlist until current_song matches value_to_remove
        while rotated_song != None:
            if rotated_song.get_value() == value_to_remove:
                song_to_remove = rotated_song
                break
            rotated_song = rotated_song.get_next_song()

        # Conditionals to either:
        if song_to_remove == None: # Return none if song doesn't exist
            return None
        elif song_to_remove == self.head_song: # Call remove_head() function if song is head
            self.remove_head()
        elif song_to_remove == self.tail_song: # Call remove_tail() function if song is tail
            self.remove_tail()
        else: # Manually switch pointers of surroundig songs
            next_song = song_to_remove.get_next_song()
            prev_song = song_to_remove.get_prev_song()
            prev_song.set_next_song(next_song)
            next_song.set_prev_song(prev_song)

        return song_to_remove


    # Loop through entire playlist and print out the values (song names)  
    def stringify_list(self):
        string_list = ""
        current_song = self.head_song
        count = 1
        while current_song:
            if current_song.get_value() != None:
                string_list += f'{str(count)}. {str(current_song.get_value()[1])}\n'
                current_song = current_song.get_next_song()
            count += 1
        return string_list