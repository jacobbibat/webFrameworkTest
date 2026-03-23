import random #Used for shuffling


class Artist:
    def __init__(self, name, dob, country, albums=None, songs=None):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = albums if albums is not None else []
        self.songs = songs if songs is not None else []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def display_info(self):
        print("Artist Information")
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Country:", self.country)
        print("Albums:", [album.album_title for album in self.albums])
        print("Songs:", [song.song_title for song in self.songs])


class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release

    def display_info(self):
        print("Song Information")
        print("Title:", self.song_title)
        print("Artist:", self.artist_name)
        print("Year of Release:", self.year_of_release)


class Album:
    def __init__(self, album_title, artist_name, year_of_release, songs=None):
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.songs = songs if songs is not None else []

    def add_song(self, title, release_year):
        new_song = Song(title, self.artist_name, release_year)
        self.songs.append(new_song)

    def display_info(self):
        print("Album Information")
        print("Title:", self.album_title)
        print("Artist:", self.artist_name)
        print("Year of Release:", self.year_of_release)
        print("Songs:", [song.song_title for song in self.songs])


class Playlist:
    def __init__(self, playlist_title, songs=None):
        self.playlist_title = playlist_title
        self.songs = songs if songs is not None else []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print("Playlist Information")
        print("Title:", self.playlist_title)
        for song in self.songs:
            print(song.song_title, "-", song.artist_name, "-", song.year_of_release)

    def sort_playlist(self, order="ASC"):
        if order == "ASC":
            self.songs.sort(key=lambda song: song.song_title)
        elif order == "DES":
            self.songs.sort(key=lambda song: song.song_title, reverse=True)
        else:
            print("Invalid order. Use ASC or DES")

    def shuffle_playlist(self):
        random.shuffle(self.songs)


#########################################################################################
########################################TEST#############################################
#########################################################################################

if __name__ == "__main__":

    # Creating an artist
    artist1 = Artist("XXXTentacion", "22/6/2000", "USA")

    # Create songs
    song1 = Song("Look at Me!", "XXXTentacion", 2016)
    song2 = Song("BAD!", "XXXTentacion", 2018)
    song3 = Song("Moonlight", "XXXTentacion", 2018)

    # Wire songs to artist
    artist1.add_song(song1)
    artist1.add_song(song2)
    artist1.add_song(song3)

    # Create album
    album1 = Album("17", "XXXTentacion", 2017)

    # Add songs to album using add_song() method
    album1.add_song("Jocelyn Flores", 2017)
    album1.add_song("Save Me", 2017)

    # Add album to artist
    artist1.add_album(album1)

    # Create playlist
    playlist1 = Playlist("Best of XXXTentacion")

    # Add songs already created
    playlist1.add_song(song1)
    playlist1.add_song(song2)
    playlist1.add_song(song3)

    # Add all songs from the album to the playlist
    for song in album1.songs:
        playlist1.add_song(song)

    # Display info
    artist1.display_info()
    print()

    song1.display_info()
    print()

    album1.display_info()
    print()

    # Print all playlist songs
    playlist1.print_all_song()
    print()

    # Sort playlist ascending
    print("Playlist sorted ASC")
    playlist1.sort_playlist("ASC")
    playlist1.print_all_song()
    print()

    # Sort playlist descending
    print("Playlist sorted DES")
    playlist1.sort_playlist("DES")
    playlist1.print_all_song()
    print()

    # Shuffle playlist
    print("Shuffled Playlist")
    playlist1.shuffle_playlist()
    playlist1.print_all_song()

