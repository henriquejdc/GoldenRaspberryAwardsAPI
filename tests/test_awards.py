from fastapi.testclient import TestClient
from app.main import app

def test_award_intervals():
    with TestClient(app) as client:
        response = client.get("/awards/intervals")
        assert response.status_code == 200
        data = response.json()
        assert data == {
            "min": [
                {
                  "producer": "Joel Silver",
                  "interval": 1,
                  "previousWin": 1990,
                  "followingWin": 1991
                }
            ],
            "max": [
                {
                  "producer": "Matthew Vaughn",
                  "interval": 13,
                  "previousWin": 2002,
                  "followingWin": 2015
                }
            ]
        }
