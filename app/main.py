import os

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .database import SessionLocal, init_db, reset_db
from .utils import load_csv_to_db
from .service import get_award_intervals

ENV = os.getenv("ENV", "dev")

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    app.state.db = db
    init_db()
    load_csv_to_db(db)
    yield
    reset_db()
    db.close()
app = FastAPI(lifespan=lifespan)

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")

@app.get("/awards/intervals", tags=["Awards"])
def read_intervals():
    db = app.state.db
    return get_award_intervals(db)
