from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql://postgres:1234@localhost:5432/chinook", echo=True)
base = declarative_base()

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))
    
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# artists = session.query(Artist)
# for artist in artists:
    # print(artist.ArtistId, artist.Name, sep = " | ")

# artists = session.query(Artist)
# for artist in artists:
    # print(artist.Name, sep = " | ")

# artist = session.query(Artist).filter_by(Name="Foo Fighters").first()
# print(artist.ArtistId, artist.Name, sep = " | ")

# artist = session.query(Artist).filter_by(ArtistId=84).first()
# print(artist.ArtistId, artist.Name, sep = " | ")

# albums = session.query(Album).filter_by(ArtistId=84)
# for album in albums:
    # print(album.AlbumId, album.Title, album.ArtistId, sep = " | ")

tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.Composer, sep = " | ")