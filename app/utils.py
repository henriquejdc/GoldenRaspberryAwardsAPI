import csv
import os

from .models import Movie
from .database import SessionLocal

ENV = os.getenv("ENV", "dev")

def load_csv_to_db(db: SessionLocal):
    data_path = "data/test/movielist.csv" if ENV == "test" else "data/movielist.csv"
    path = os.path.join(os.path.dirname(__file__), data_path)
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            movie = Movie(
                year=int(row["year"]),
                title=row["title"],
                studios=row["studios"],
                producers=row["producers"],
                winner=row["winner"].strip().lower() == "yes"
            )
            db.add(movie)
        db.commit()
