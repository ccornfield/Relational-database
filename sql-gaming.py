from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql://postgres:1234@localhost:5432/chinook", echo=True)
base = declarative_base()

class Video_Game(base):
    __tablename__ = "Video Game",
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_year = Column(Integer, primary_key=False)
    genre = Column(String)
    console = Column(String)
    developer = Column(String)
    publisher = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

command_and_conquer = Video_Game(
    name = "Command & Conquer: Red Alert",
    release_year = 1998,
    genre = "RTS",
    console = "PS1",
    developer = "Westwood Studios",
    publisher = "Virgin Interactive"
)

metal_slug = Video_Game(
    name = "Metal Slug 4",
    release_year = 2002,
    genre = "Run N Gun",
    console = "Arcade",
    developer = "Mega Enterprise",
    publisher = "Playmore"
)

black_ops = Video_Game(
    name = "Call of Duty: Black Ops",
    release_year = 2010,
    genre = "FPS",
    console = "Xbox 360",
    developer = "Treyarch",
    publisher = "Activision"
)

payday = Video_Game(
    name = "Payday 2",
    release_year = 2013,
    genre = "Co-op FPS",
    console = "PC",
    developer = "Overkill Software",
    publisher = "505 Games"
)

battlefield = Video_Game(
    name = "Battlefield 1",
    release_year = 2016,
    genre = "FPS",
    console = "Xbox One",
    developer = "DICE",
    publisher = "Electronic Arts"
)

team_fortress = Video_Game(
    name = "Team Fortress 2",
    release_year = 2007,
    genre = "Multiplayer FPS",
    console = "PC",
    developer = "Valve",
    publisher = "Valve"
)

session.add(command_and_conquer)
session.add(metal_slug)
session.add(black_ops)
session.add(payday)
session.add(battlefield)
session.add(team_fortress)

session.commit()

video_games = session.query(Video_Game)
for video_game in video_games:
    print(
        video_game.id,
        video_game.name,
        video_game.release_year,
        video_game.genre,
        video_game.console,
        video_game.developer,
        video_game.publisher,
        sep= " | "
    )

