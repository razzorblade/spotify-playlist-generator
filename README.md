

# Spotify Playlist Generator

Convert any text file into a Spotify playlist effortlessly!

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

The **Spotify Playlist Generator** is a Python-based tool that allows you to seamlessly convert a list of song titles from a text file into a Spotify playlist. Whether you have your favorite songs documented or want to organize your music library, this tool simplifies the process by leveraging Spotify's Web API to search and add tracks to your desired playlist.

## Features

- **Automated Song Addition:** Iterate through a text file line by line and add each song to a specified Spotify playlist.
- **Intelligent Search:** Utilize Spotify's API to search for songs, effectively handling typos and inconsistently formatted text.
- **Duplicate Prevention:** Automatically checks for existing tracks in the playlist to prevent duplicate entries.
- **Playlist Management:** Create new playlists or update existing ones with new tracks.
- **Command-Line Interface:** Easily interact with the tool using simple command-line arguments.
- **Customizable:** Specify input files and playlist names dynamically without modifying the script.

## Requirements

- **Python:** Version 3.11 is required.
- **Spotipy Library:** Install via pip.

  ```bash
  pip install spotipy
  ```

- **Spotify Developer Account:**
  - **App Creation:**
    - Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
    - Click on **"Create an App"** to obtain your **Client ID** and **Client Secret**.
  - **Redirect URI:**
    - Set the Redirect URI to `http://localhost:8888/callback` in your app settings.
    - This URI must match exactly with the one specified in your script.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/spotify-playlist-generator.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd spotify-playlist-generator
   ```

3. **Install Required Libraries:**

   Ensure you have `spotipy` installed:

   ```bash
   pip install spotipy
   ```

## Configuration

1. **Obtain Spotify API Credentials:**

   - **Client ID and Client Secret:**
     - After creating your app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard), you will receive a **Client ID** and **Client Secret**.

2. **Update the Script with Your Credentials:**

   Open the `script.py` file and replace the placeholder values with your actual Spotify credentials:

   ```python
   # Replace these with your Spotify app credentials
   CLIENT_ID = 'your_spotify_client_id'
   CLIENT_SECRET = 'your_spotify_client_secret'
   REDIRECT_URI = 'http://localhost:8888/callback'  # Ensure this matches your Spotify app settings
   ```

## Usage

Run the script using the command line, specifying the input file and the desired playlist name.

### Command Syntax

```bash
python script.py -i <path_to_file> -p <playlist_name>
```

### Parameters

- `-i`, `--input`: **(Required)** Path to the input text file containing song titles.
- `-p`, `--playlist`: **(Required)** Name of the Spotify playlist to create or update.

### Example

```bash
python script.py -i songs.txt -p "My Favorite Songs"
```

This command will read each song title from `songs.txt` and add them to a Spotify playlist named "My Favorite Songs". If the playlist already exists, it will update it by adding only the new tracks that are not already present.

## Example

### Sample `songs.txt` File

Create a text file named `songs.txt` with each song title on a new line:

```
Shape of You
Blinding Lights
Levitating - Dua Lipa
Bad Guy by billie eilish
Dance Monkey
Eniru - Favourite Song
```

### Running the Script

Execute the following command in your terminal:

```bash
python script.py -i songs.txt -p "Chill Vibes"
```

### Expected Output

```
Playlist 'Chill Vibes' already exists. Adding new tracks to it.
'Shape of You' by Ed Sheeran is already in the playlist.
Will add 'Blinding Lights' by The Weeknd
Will add 'Levitating' by Dua Lipa
'Bad Guy' by Billie Eilish is already in the playlist.
'Dance Monkey' by Tones and I is already in the playlist.
'Favourite Song' by Eniru is already in the playlist.

Added 2 new tracks to 'Chill Vibes'.
```

In this example:

- The script identifies that the playlist "Chill Vibes" already exists.
- It checks each song in `songs.txt`:
  - If the song is already in the playlist, it skips adding it.
  - If the song is not in the playlist, it adds the song and notifies the user.
- Finally, it summarizes the number of new tracks added.


## License

This project is licensed under the [MIT License](LICENSE).

---

*Developed with ❤️ by [razzorblade](https://github.com/razzorblade)*
