# Playlist Manager

A simple command-line application to manage and play your favorite songs using a linked list structure. The application integrates with Spotify to search for tracks and control playback.

![image](https://github.com/user-attachments/assets/cffd4a0b-8acd-4099-8ada-f93c8de105d0)


## Features

- **Play and Pause:** Start and pause playback of songs.
- **Add and Remove Songs:** Manage your playlist by adding new songs or removing existing ones.
- **Skip and Go Back:** Navigate through the playlist with ease.
- **Display Current Song:** Always see what’s currently playing.
- **User-Friendly Menu:** Clear instructions and feedback for commands.

## Requirements

- Python 3.x
- External libraries (ensure you have `LinkedLists` and `spotifyRequests` modules properly set up).
- Spotify Premium Account

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Install dependencies:
   ```bash
   pip install spotipy
   pip install dotenv
4. Open a Spotify tab on your computer, or phone, on the same account you logged in with in the credentials.env file.

## Usage
- play: Start playing the playlist.
- pause: Pause the current song.
- add: Add a new song by typing its name.
- remove: Remove a song from the playlist.
- skip: Skip to the next song.
- prev: Go back to the previous song.
- playlist: Show the full playlist.
- exit: Exit the application.

## Setting Up Spotify Credentials

To integrate the application with your Spotify account, you'll need to provide your own Spotify API credentials. Follow these steps to set up the necessary environment variables:

1. **Create a Spotify Developer Account:**
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login).
   - Log in with your Spotify account or create a new account if you don’t have one.

2. **Create a New Application:**
   - Click on "Create an App."
   - Fill in the required information (App name, description, etc.).
   - Accept the terms and conditions and click "Create."

3. **Obtain Your Client ID and Client Secret:**
   - After creating the app, you'll be taken to the app's dashboard.
   - You will see your **Client ID** and **Client Secret** on this page. Click on "Show Client Secret" to reveal it.

4. **Set the Redirect URI:**
   - In the app settings, find the **Redirect URIs** section.
   - Add a redirect URI, which is usually something like `http://localhost:8888/callback`. This URI must match the one specified in your application.

5. **Set Environment Variables:**
   You can set the environment variables in your terminal or create a `.env` file in your project directory.

   - If using a terminal, you can set them like this:
     ```bash
     export SPOTIPY_CLIENT_ID="your_client_id_here"
     export SPOTIPY_CLIENT_SECRET="your_client_secret_here"
     export SPOTIPY_REDIRECT_URI="your_redirect_uri_here"
     ```

   - If you prefer to use a `.env` file, create a file named `.env` in the root of your project and add the following lines:
     ```env
     SPOTIPY_CLIENT_ID=your_client_id_here
     SPOTIPY_CLIENT_SECRET=your_client_secret_here
     SPOTIPY_REDIRECT_URI=your_redirect_uri_here
     ```

6. **Install the Python Dotenv Package (if using .env):**
   If you created a `.env` file, ensure you have the `python-dotenv` package installed to load environment variables from the file. You can install it using:
   ```bash
   pip install python-dotenv

