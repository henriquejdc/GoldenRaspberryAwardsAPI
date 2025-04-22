from collections import defaultdict
from .database import SessionLocal
from .models import Movie

def get_award_intervals(db: SessionLocal):
    producer_years = defaultdict(list)
    
    for movie in db.query(Movie).filter(Movie.winner == True).all():
        for producer in map(str.strip, movie.producers.replace(" and ", ",").split(",")):
            producer_years[producer].append(movie.year)

    result = []

    for producer, years in producer_years.items():
        if len(years) < 2:
            continue

        sorted_years = sorted(years)
        for i in range(1, len(sorted_years)):  # type: ignore
            result.append({
                "producer": producer,
                "interval": sorted_years[i] - sorted_years[i-1],
                "previousWin": sorted_years[i-1],
                "followingWin": sorted_years[i],
            })

    if not result:
        return {"min": [], "max": []}

    min_interval = min(result, key=lambda x: x["interval"])["interval"]
    max_interval = max(result, key=lambda x: x["interval"])["interval"]

    return {
        "min": [r for r in result if r["interval"] == min_interval],
        "max": [r for r in result if r["interval"] == max_interval]
    }
