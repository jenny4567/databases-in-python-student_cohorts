from lib.album import Album

"""
Album constructs with an id, title, release_year, artist_id
"""
def test_album_constructs():
    album = Album(1, "Waterloo", 1974, 2)
    assert album.id == 1
    assert album.title == "Waterloo"
    assert album.release_year == 1974
    assert album.artist_id == 2

"""
We can format albums to strings nicely
"""
def test_album_format_nicely():
    album = Album(1, "Waterloo", 1974, 2)
    assert str(album) == "Album(1, Waterloo, 1974, 2)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Waterloo", 1974, 2)
    album2 = Album(1, "Waterloo", 1974, 2)
    assert album1 == album2

"""
We can compare two different albums
And have them be not equal
"""
def test_albums_are_unequal():
    album1 = Album(1, "Waterloo", 1974, 2)
    album2 = Album(1, "Waterloo - remastered", 1998, 2)
    assert album1 != album2