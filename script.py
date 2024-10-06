import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your Spotify app credentials
CLIENT_ID = '<id>'
CLIENT_SECRET = '<secret>'
REDIRECT_URI = 'http://localhost:8888/callback'  # Ensure this matches your Spotify app settings

# Define the scope
SCOPE = 'playlist-modify-public playlist-modify-private'

def main(input_file, playlist_name):
    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=SCOPE))

    # Read song titles from the input file with explicit encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        song_titles = [line.strip() for line in file if line.strip()]

    # Get the current user's ID
    user_id = sp.current_user()['id']

    # Check if the playlist already exists
    playlist_id = None
    playlists = sp.current_user_playlists(limit=50)
    while playlists:
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                playlist_id = playlist['id']
                break
        if playlists['next'] and not playlist_id:
            playlists = sp.next(playlists)
        else:
            break

    if playlist_id:
        print(f"Playlist '{playlist_name}' already exists. Adding new tracks to it.")
    else:
        # Create a new playlist with the specified name
        playlist = sp.user_playlist_create(user=user_id, name=playlist_name)
        playlist_id = playlist['id']
        print(f"Created new playlist '{playlist_name}'.")

    # Get the track IDs currently in the playlist
    existing_track_ids = set()
    results = sp.playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track and track['id']:
                existing_track_ids.add(track['id'])
        if results['next']:
            results = sp.next(results)
        else:
            break

    # Search for songs and prepare a list of new tracks to add
    track_ids_to_add = []
    for title in song_titles:
        # Search for the song on Spotify
        results = sp.search(q=title, limit=1, type='track')
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_id = track['id']
            if track_id not in existing_track_ids:
                track_ids_to_add.append(track_id)
                print(f"Will add '{track['name']}' by {track['artists'][0]['name']}")
            else:
                print(f"'{track['name']}' by {track['artists'][0]['name']}' is already in the playlist.")
        else:
            print(f"Song '{title}' not found on Spotify.")

    # Add new tracks to the playlist
    if track_ids_to_add:
        sp.playlist_add_items(playlist_id=playlist_id, items=track_ids_to_add)
        print(f"\nAdded {len(track_ids_to_add)} new tracks to '{playlist_name}'.")
    else:
        print(f"\nNo new tracks to add to '{playlist_name}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add songs from a file to a Spotify playlist.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input file containing song titles.')
    parser.add_argument('-p', '--playlist', required=True, help='Name of the playlist to create or update.')
    args = parser.parse_args()

    main(args.input, args.playlist)
