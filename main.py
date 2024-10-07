import os
import time
from LinkedLists import Song, Playlist
from spotifyRequests import search_track_uri, play_song, pause_song, currently_playing

# ANSI escape codes for colors and styles
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# SongPlayer class that handles song playing functionalities
class SongPlayer(Playlist):
    def __init__(self):
        super().__init__()
        self.current = self.head_song  # Initially head song is playing
        self.timestamp = 0

    # Start playing from the first song in the playlist
    def play(self):
        if self.head_song: # If playlist exists
            if not self.current: # If self.current doesnt exists (first iteration)
                self.current = self.head_song
                
            print(f"{GREEN}▶️  Playing: {BOLD}{self.current.get_value()[1]}{RESET}")

            # Play the song if a track was found
            local_track_data = self.current.get_value()
            play_song(local_track_data[0], local_track_data[1], self.timestamp)

        else:
            print(f"{RED}⚠️  The playlist is empty, add songs to play.{RESET}")
            time.sleep(2)
    
    # Pause current song
    def pause(self):
        self.timestamp = pause_song()  # Update the instance variable

    # Display the current song in a formatted style
    def display_current(self):
        current = currently_playing()
        if current:
            print(f"\n{MAGENTA}🎵 Currently playing: {BOLD}{current}{RESET}")
        else:
            print(f"{YELLOW}No song is currently playing.{RESET}")

    # Skip to the next song
    def skip(self):
        if self.current and self.current.get_next_song():
            self.current = self.current.get_next_song()
            play_song(self.current.get_value()[0], self.current.get_value()[1])
            print(f"{CYAN}⏩  Skipping to: {BOLD}{self.current.get_value()[1]}{RESET}")
        else:
            print(f"{RED}⚠️  No next song available to skip to.{RESET}")
            time.sleep(2)

    # Go back to the previous song
    def prev(self):
        if self.current and self.current.get_prev_song():
            self.current = self.current.get_prev_song()
            play_song(self.current.get_value()[0], self.current.get_value()[1])
            print(f"{CYAN}⏪  Going back to: {BOLD}{self.current.get_value()[1]}{RESET}")
        else:
            print(f"{RED}⚠️  No previous song available to go back to.{RESET}")
            time.sleep(2)

# Prints commands the user can use with visual enhancement
def show_menu():
    print("\n" + "="*40)
    print(f"{BOLD}{CYAN}🎶  Welcome to Your Playlist Manager  🎶{RESET}")
    print("="*40)
    print(f"{UNDERLINE}Available Commands:{RESET}")
    print(f"  {GREEN}  'play'{RESET}     - Start playing the playlist")
    print(f"  {CYAN}  'pause'{RESET}    - Pause the song")
    print(f"  {GREEN}  'add'{RESET}      - Add a new song to the playlist")
    print(f"  {RED}  'remove'{RESET}   - Remove an existing song")
    print(f"  {YELLOW}  'skip'{RESET}     - Skip to the next song")
    print(f"  {YELLOW}  'back'{RESET}     - Go back to the previous song")
    print(f"  {WHITE}  'playlist'{RESET} - Show the full playlist")
    print(f"  {RED}  'exit'{RESET}     - Exit the Playlist Manager")
    print("="*40)


# UI to send requests
def handle_input(playlist):
    while True:
        os.system('clear')  # Clears the terminal window to keep the UI clean
        show_menu()

        # Display the current song right below the menu
        playlist.display_current()

        # Wait for user input
        inp = input(f"\n{BOLD}Enter your command:{RESET} ").strip().lower()

        if inp == 'play':
            playlist.play()

        elif inp == 'pause':
            playlist.pause()

        elif inp == 'add':
            song_name = input(f'{GREEN}🎶  Type the name of the song you want to add: {RESET}')
            track_data = search_track_uri(song_name)
            if track_data:
                playlist.add_to_tail(track_data)
                print(f"{GREEN}➕  '{track_data[1]}' has been added to the playlist.{RESET}")
            time.sleep(1.5)  # Adding delay for smooth UI experience

        elif inp == 'remove':
            song_name = input(f'{RED}❌ Type the name of the song you would like to remove: {RESET}')
            removed_song = playlist.remove_by_value(song_name)
            if removed_song:
                print(f"{RED}Removed '{removed_song.get_value()}'{RESET}")
            else:
                print(f"{YELLOW}Song not found{RESET}")
            time.sleep(2)

        elif inp == 'skip':
            playlist.skip()
            time.sleep(1)

        elif inp == 'prev':
            playlist.prev()
            time.sleep(1)

        elif inp == 'playlist':
            list = playlist.stringify_list()
            if list == "":
                print(f'{RED}No songs are currently in the playlist❗❗{RESET}')
            else:
                print(f"{BOLD}{WHITE}Current Playlist:{RESET}\n{list}")
            input(f"{CYAN}Press Enter to continue... {RESET}")

        elif inp == 'exit':
            print(f"{RED}👋  Exiting the Playlist Manager. Goodbye!{RESET}")
            break

        else:
            print(f"{YELLOW}⚠️  Invalid option, please try again.{RESET}")
            time.sleep(1)


# Initialize Playlist Manager
playlist = SongPlayer()
handle_input(playlist)