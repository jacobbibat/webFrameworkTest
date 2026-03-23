import unittest
from partA import Artist, Song, Album, Playlist


class TestMusicPlaylist(unittest.TestCase):

    # Test if object IS instance of class 

    def test_artist_is_instance_of_artist(self):
        artist = Artist("XXXTentacion", "22/6/2000", "USA")
        self.assertIsInstance(artist, Artist)

    def test_song_is_instance_of_song(self):
        song = Song("SAD!", "XXXTentacion", 2017)
        self.assertIsInstance(song, Song)

    def test_album_is_instance_of_album(self):
        album = Album("17", "XXXTentacion", 2017)
        self.assertIsInstance(album, Album)

    def test_playlist_is_instance_of_playlist(self):
        playlist = Playlist("My Playlist")
        self.assertIsInstance(playlist, Playlist)

    # Test if object is NOT instance of class 

    def test_artist_is_not_instance_of_song(self):
        artist = Artist("XXXTentacion", "22/6/2000", "USA")
        self.assertNotIsInstance(artist, Song)

    def test_song_is_not_instance_of_album(self):
        song = Song("SAD!", "XXXTentacion", 2017)
        self.assertNotIsInstance(song, Album)

    def test_album_is_not_instance_of_playlist(self):
        album = Album("17", "XXXTentacion", 2017)
        self.assertNotIsInstance(album, Playlist)

    def test_playlist_is_not_instance_of_artist(self):
        playlist = Playlist("My Playlist")
        self.assertNotIsInstance(playlist, Artist)

    # Test identical and unidentical but similar objects 

    def test_identical_objects(self):
        song1 = Song("Moonlight", "XXXTentacion", 2018)
        song2 = song1
        self.assertIs(song1, song2)

    def test_similar_but_not_identical_objects(self):
        song1 = Song("Moonlight", "XXXTentacion", 2018)
        song2 = Song("Moonlight", "XXXTentacion", 2018)
        self.assertIsNot(song1, song2)

    # Test add_song() and add_album() methods 

    def test_artist_add_song(self):
        artist = Artist("XXXTentacion", "22/6/2000", "USA")
        song = Song("Look at Me!", "XXXTentacion", 2016)
        artist.add_song(song)
        self.assertIn(song, artist.songs)

    def test_artist_add_album(self):
        artist = Artist("XXXTentacion", "22/6/2000", "USA")
        album = Album("17", "XXXTentacion", 2017)
        artist.add_album(album)
        self.assertIn(album, artist.albums)

    def test_album_add_song(self):
        album = Album("17", "XXXTentacion", 2017)
        album.add_song("Jocelyn Flores", 2017)
        self.assertEqual(len(album.songs), 1)
        self.assertEqual(album.songs[0].song_title, "Jocelyn Flores")

    def test_playlist_add_song(self):
        playlist = Playlist("Best of XXXTentacion")
        song = Song("SAD!", "XXXTentacion", 2017)
        playlist.add_song(song)
        self.assertIn(song, playlist.songs)

    # Test sort_playlist() and shuffle_playlist()

    def test_sort_playlist_ascending(self):
        playlist = Playlist("Test Playlist")
        song1 = Song("Moonlight", "XXXTentacion", 2018)
        song2 = Song("BAD!", "XXXTentacion", 2018)
        song3 = Song("SAD!", "XXXTentacion", 2017)

        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)

        playlist.sort_playlist("ASC")

        self.assertEqual(playlist.songs[0].song_title, "BAD!")
        self.assertEqual(playlist.songs[1].song_title, "Moonlight")
        self.assertEqual(playlist.songs[2].song_title, "SAD!")

    def test_sort_playlist_descending(self):
        playlist = Playlist("Test Playlist")
        song1 = Song("Moonlight", "XXXTentacion", 2018)
        song2 = Song("BAD!", "XXXTentacion", 2018)
        song3 = Song("SAD!", "XXXTentacion", 2017)

        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)

        playlist.sort_playlist("DES")

        self.assertEqual(playlist.songs[0].song_title, "SAD!")
        self.assertEqual(playlist.songs[1].song_title, "Moonlight")
        self.assertEqual(playlist.songs[2].song_title, "BAD!")

    def test_shuffle_playlist(self):
        playlist = Playlist("Test Playlist")
        song1 = Song("Moonlight", "XXXTentacion", 2018)
        song2 = Song("BAD!", "XXXTentacion", 2018)
        song3 = Song("SAD!", "XXXTentacion", 2017)

        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)

        songs_before_shuffle = playlist.songs.copy()
        playlist.shuffle_playlist()
        songs_after_shuffle = playlist.songs

        self.assertCountEqual(songs_before_shuffle, songs_after_shuffle)


if __name__ == "__main__":
    unittest.main()
