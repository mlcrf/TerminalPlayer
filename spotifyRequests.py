import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

# Load environment variables from .env file for security measures
load_dotenv(os.path.join(os.path.dirname(__file__), 'credentials.env'))

SCOPE = 'user-modify-playback-state user-read-playback-state user-library-read '

# Spotify API credentials (from your Spotify Developer Dashboard)
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Set up authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=SCOPE))

# Function to get available devices
def get_available_devices():
    devices = sp.devices()
    if devices['devices']:
        return devices['devices'][0]['id']  # Get the first available device ID
    else:
        print("No devices available")
        return None

# Function to play a song
def play_song(track_uri, track_name, progress_ms=0):
    global device_id
    try:
        # Get the available device ID
        device_id = get_available_devices()

        if not device_id:
            print("No device found to play the song")
            return

        # Determine if the song should be resumed or started from the beginning
        sp.start_playback(device_id=device_id, uris=[track_uri], position_ms=progress_ms if progress_ms > 0 else 0)

        # Log playback status
        print(f"Playing: {track_name}")

    except Exception as e:
        print(f"Error playing the song: {e}")

def pause_song():
    current_playback = sp.current_playback()
    sp.pause_playback()
    return current_playback['progress_ms']

def currently_playing():
    current_track = sp.current_playback()
    if current_track and current_track['is_playing']:
        return f"{current_track['item']['name']} by {current_track['item']['artists'][0]['name']}"
    else:
        return False

# Function to search for track URIs by track name
def search_track_uri(track_name, limit=5):
    results = sp.search(q=track_name, type='track', limit=limit)
    tracks = results['tracks']['items']
    
    if tracks:
        print('\nChoose which song (1/2/3/4/5): ')
        for idx, track in enumerate(tracks):
            print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}\n")
        
        while True:
            try:
                track_choice = int(input('Which track do you want to add? '))
                if 1 <= track_choice <= len(tracks):
                    selected_track = tracks[track_choice - 1]
                    return [selected_track['uri'], f"{selected_track['name']} by {selected_track['artists'][0]['name']}"]
                else:
                    print("Please select a valid track number.")
            except ValueError:
                print("Please enter a number.")

    else:
        print("No tracks found for your search.")
        return None